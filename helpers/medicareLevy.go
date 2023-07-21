package helpers

// Doesn't calculate ML Surcharge or ML Reduction yet
func CalcMedicareLevy(taxableIncome float64, single bool, paysMedicareLevySurcharge bool) float64 {

	// Exempt from Medicare Levy
	if single && taxableIncome <= 23365 {
		return 0
	}

	// Standard Medicare Levy
	medicareLevy := taxableIncome * 0.02

	if paysMedicareLevySurcharge {
		medicareLevy = medicareLevy + (taxableIncome * 0.01)
	}

	return medicareLevy
}

func PaysMedicareLevySurcharge(taxableIncome float64, single bool, privateHealthCover bool) bool {
	// TODO: Take private health cover into account
	return taxableIncome > 90000 && single
}
