package cmd

import (
	"fmt"
	"os"

	"github.com/AlecAivazis/survey/v2"
	"github.com/spf13/cobra"
	"github.com/tobyscott25/eofy-calc/helpers"
)

var CmdCalculateTax = &cobra.Command{
	Use:   "tax",
	Short: "Calculate tax",
	Long:  `A fast income tax calulator for Australians, written in Go by Toby Scott.`,
	Run: func(cmd *cobra.Command, args []string) {

		questions := []*survey.Question{
			{
				Name:   "GrossAnnualSalary",
				Prompt: &survey.Input{Message: "Your annual salary (eg. 65000 = $65,000)", Default: os.Getenv("PFC_GROSS_SALARY")},
			},
			{
				Name:   "SalarySacrificePercent",
				Prompt: &survey.Input{Message: "How much are you salary sacrificing? (eg. 10 = 10%)", Default: os.Getenv("PFC_SALARY_SACRIFICE_PERCENTAGE")},
			},
			{
				Name:   "HasHecsHelpDebt",
				Prompt: &survey.Confirm{Message: "Do you have a HECS/HELP debt?", Default: os.Getenv("PFC_HAS_HELP_DEBT") == "true"},
			},
			{
				Name:   "HasPrivHealthCover",
				Prompt: &survey.Confirm{Message: "Do you have private health insurance?", Default: os.Getenv("PFC_HAS_PRIVATE_HEALTH_COVER") == "true"},
			},
			{
				Name:   "Single",
				Prompt: &survey.Confirm{Message: "Are you single? (not married or in a de facto relationship)", Default: os.Getenv("PFC_SINGLE") == "true"},
			},
			{
				Name:   "NumberOfDependants",
				Prompt: &survey.Input{Message: "How many dependants do you have?", Default: os.Getenv("PFC_NUMBER_OF_DEPENDANTS")},
			},
			{
				Name:   "SaptoEligible",
				Prompt: &survey.Confirm{Message: "Are you eligible for the seniors and pensioners tax offset (SAPTO)?", Default: os.Getenv("PFC_SAPTO_ELIGIBLE") == "true"},
			},
		}

		answers := struct {
			GrossAnnualSalary      int
			SalarySacrificePercent int
			HasHecsHelpDebt        bool
			HasPrivHealthCover     bool
			Single                 bool // Does not have a spouse (married or de facto)
			NumberOfDependants     int
			SaptoEligible          bool // Are you eligible for the seniors and pensioners tax offset (SAPTO)?
		}{}

		err := survey.Ask(questions, &answers)
		if err != nil {
			fmt.Println(err)
			return
		}

		// Run calculations
		salarySacrificeAmount := answers.GrossAnnualSalary * answers.SalarySacrificePercent / 100
		taxableIncome := helpers.CalcTaxableIncome(answers.GrossAnnualSalary, answers.SalarySacrificePercent)
		incomeTax := helpers.CalcIncomeTax(float64(taxableIncome))
		hecsRepaymentRate := helpers.CalcHecsHelpRepaymentRate(answers.GrossAnnualSalary) // Repayment rate is based on your gross salary, not taxable income.
		hecsRepaymentAmount := float64(answers.GrossAnnualSalary) * hecsRepaymentRate
		paysMedicareLevySurcharge := helpers.PaysMedicareLevySurcharge(float64(taxableIncome), answers.Single, answers.HasPrivHealthCover)
		medicareLevy := helpers.CalcMedicareLevy(float64(taxableIncome), answers.Single, paysMedicareLevySurcharge)

		// Print out report
		fmt.Println("=====================================")
		fmt.Printf("Your gross annual salary is %s\n", helpers.FormatAsCurrency(float64(answers.GrossAnnualSalary)))
		fmt.Printf("You are salary sacrificing %s (%d%%)\n", helpers.FormatAsCurrency(float64(salarySacrificeAmount)), answers.SalarySacrificePercent)
		fmt.Printf("Your taxable income is %s\n", helpers.FormatAsCurrency(float64(taxableIncome)))
		fmt.Println("=====================================")
		fmt.Printf("Your income tax is %s\n", helpers.FormatAsCurrency(float64(incomeTax)))
		fmt.Printf("Your medicare levy is %s\n", helpers.FormatAsCurrency(float64(medicareLevy)))
		if answers.HasHecsHelpDebt {
			fmt.Printf("You have a HELP/HECS debt, your HECS repayment is %s (%s%% of %s)\n", helpers.FormatAsCurrency(float64(hecsRepaymentAmount)), (helpers.FormatAsCurrency(float64(hecsRepaymentRate * 100))), helpers.FormatAsCurrency(float64(answers.GrossAnnualSalary)))
		}
		fmt.Println("=====================================")
		fmt.Printf("Total going to the ATO: %s\n", helpers.FormatAsCurrency(float64(incomeTax+medicareLevy+hecsRepaymentAmount)))
		fmt.Printf("Salary sacrifice amount: %s\n", helpers.FormatAsCurrency(float64(salarySacrificeAmount)))
		fmt.Printf("Total take home pay: %s\n", helpers.FormatAsCurrency(float64(float64(answers.GrossAnnualSalary)-(incomeTax+medicareLevy+hecsRepaymentAmount)-float64(salarySacrificeAmount))))
		fmt.Println("=====================================")
	},
}
