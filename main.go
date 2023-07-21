package main

import (
	"fmt"

	"github.com/tobyscott25/eofy-calc/helpers"
)

func main() {
	fmt.Println("Welcome to EOFY Calculator!")

	// Retreive required details
	salary := helpers.IntInputLoop("What is your annual salary? (eg. 55000 = $55,000): ")
	salarySacrificePercentage := helpers.IntInputLoop("How much are you salary sacrificing? (eg. 10 = 10%): ")
	hasHelpDebt := helpers.BoolInputLoop("Do you have a HELP/HECS debt? (true/false): ")
	hasPrivateHealthCover := helpers.BoolInputLoop("Do you have private health cover? (true/false): ") // For Medicare Levy Surcharge

	// Hard-coded values, yet to take user input for these
	single := true // Does not have a spouse (married or de facto)
	// numberOfDependants := 0
	// saptoEligible := false // Were you eligible for the seniors and pensioners tax offset (SAPTO)?

	// Run calculations
	salarySacrificeAmount := salary * salarySacrificePercentage / 100
	taxableIncome := helpers.CalcTaxableIncome(salary, salarySacrificePercentage)
	incomeTax := helpers.CalcIncomeTax(float64(taxableIncome))
	hecsRepaymentRate := helpers.CalcHecsHelpRepaymentRate(salary) // Repayment rate is based on your gross salary, not taxable income.
	hecsRepaymentAmount := float64(salary) * hecsRepaymentRate
	paysMedicareLevySurcharge := helpers.PaysMedicareLevySurcharge(float64(taxableIncome), single, hasPrivateHealthCover)
	medicareLevy := helpers.CalcMedicareLevy(float64(taxableIncome), single, paysMedicareLevySurcharge)

	// Print out report
	fmt.Println("=====================================")
	fmt.Printf("Your gross annual salary is $%d\n", salary)
	fmt.Printf("You are salary sacrificing $%d (%d%%)\n", salarySacrificeAmount, salarySacrificePercentage)
	fmt.Printf("Your taxable income is $%d\n", taxableIncome)
	fmt.Println("=====================================")
	fmt.Printf("Your income tax is $%.2f\n", incomeTax)
	fmt.Printf("Your medicare levy is $%.2f\n", medicareLevy)
	if hasHelpDebt {
		fmt.Printf("You have a HELP/HECS debt, your HECS repayment is $%.2f (%.2f%% of $%d)\n", hecsRepaymentAmount, (hecsRepaymentRate * 100), salary)
	}
	fmt.Println("=====================================")
	fmt.Printf("Total going to the ATO: $%.2f\n", (incomeTax + medicareLevy + hecsRepaymentAmount))
	fmt.Printf("Salary sacrifice amount: $%d\n", salarySacrificeAmount)
	fmt.Printf("Total take home pay: $%.2f\n", (float64(salary) - (incomeTax + medicareLevy + hecsRepaymentAmount) - float64(salarySacrificeAmount)))
	fmt.Println("=====================================")
}
