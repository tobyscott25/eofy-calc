package helpers

func CalcIncomeTax(taxableIncome float64) float64 {
	var tax float64

	if taxableIncome <= 18200 { // Up to $18,200
		tax = 0
	} else if taxableIncome <= 45000 { // Up to $45,000
		// Tax every dollar after $18,200 at 19%
		amountToTax := taxableIncome - 18200
		tax = amountToTax * 0.19

		// Add the tax from the previous bracket(s)
		tax = tax + 0
	} else if taxableIncome <= 120000 { // Up to $120,000
		// Tax every dollar after $45,000 at 32.5%
		amountToTax := taxableIncome - 45000
		tax = amountToTax * 0.325

		// Add the tax from the previous bracket(s)
		tax = tax + 5092
	} else if taxableIncome <= 180000 { // Up to $180,000
		// Tax every dollar after $120,000 at 37%
		amountToTax := taxableIncome - 120000
		tax = amountToTax * 0.37

		// Add the tax from the previous bracket(s)
		tax = tax + 29467
	} else { // Over $180,000
		// Tax every dollar after $180,000 at 45%
		amountToTax := taxableIncome - 180000
		tax = amountToTax * 0.45

		// Add the tax from the previous bracket(s)
		tax = tax + 51667
	}

	return tax
}
