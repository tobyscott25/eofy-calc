// Assumes:
// - You are buying a home in Victoria
// - You are not a foreign purchaser
// - You are not a company or trust

package cmd

import (
	"fmt"
	"os"

	"github.com/AlecAivazis/survey/v2"
	"github.com/spf13/cobra"
	fhhelpers "github.com/tobyscott25/eofy-calc/fh-helpers"
	"github.com/tobyscott25/eofy-calc/helpers"
)

var CmdFirstHomeCalculator = &cobra.Command{
	Use:   "firsthome",
	Short: "First Home Calculator for Victorians",
	Long:  `Calculate stamp duty, grants, and concessions for first home buyers in Victoria.`,
	Run: func(cmd *cobra.Command, args []string) {

		questions := []*survey.Question{
			{
				Name:   "GrossAnnualSalary",
				Prompt: &survey.Input{Message: "Your annual salary (eg. 65000 = $65,000)", Default: os.Getenv("PFC_GROSS_SALARY")},
			},
			{
				Name: "PropertyCost",
				Prompt: &survey.Input{
					Message: "What is the cost of the property?",
					Default: "600000",
				},
			},
			{
				Name: "PropertyType",
				Prompt: &survey.Select{
					Message: "Is the property new or established?",
					Options: []string{"New", "Established"},
					Default: "Established",
				},
			},
			{
				Name: "FirstHome",
				Prompt: &survey.Confirm{
					Message: "Is this your first home?",
					Default: true,
				},
			},
			{
				Name: "PrincipalResidence",
				Prompt: &survey.Confirm{
					Message: "Do you intend to live in the property as your principal place of residence?",
					Default: true,
				},
			},
			// Additional fields for new conditions later...
		}

		answers := struct {
			PropertyCost       float64
			PropertyType       string
			GrossAnnualSalary  float64
			FirstHome          bool
			PrincipalResidence bool
			// Additional fields for new conditions later...
		}{}

		err := survey.Ask(questions, &answers)
		if err != nil {
			fmt.Println(err)
			return
		}

		// Calculate the stamp duty, grants, and apply conditions based on the answers
		stampDuty := fhhelpers.CalculateStampDuty(answers.PropertyCost, answers.PropertyType, answers.FirstHome)
		grant := fhhelpers.CalculateGrant(answers.PropertyCost, answers.PropertyType, answers.FirstHome)
		fhbgEligible := fhhelpers.IsFHBGEligible(answers.GrossAnnualSalary)
		fhsssContribution := fhhelpers.CalculateFHSSS(answers.GrossAnnualSalary)

		// Output the results
		fmt.Println("=====================================")
		fmt.Printf("Cost of the property: %s\n", helpers.FormatAsCurrency(answers.PropertyCost))
		fmt.Printf("Type of property: %s\n", answers.PropertyType)
		fmt.Printf("Stamp Duty payable: %s\n", helpers.FormatAsCurrency(stampDuty))
		fmt.Printf("First Home Owner Grant: %s\n", helpers.FormatAsCurrency(grant))
		fmt.Println("=====================================")
		if fhbgEligible {
			fmt.Println("You are eligible for the First Home Buyer Grant (FHBG).")
		}
		if fhsssContribution > 0 {
			fmt.Printf("You can salary sacrifice %s this year for the FHSSS.\n", helpers.FormatAsCurrency(fhsssContribution))
		}
		fmt.Println("=====================================")
	},
}
