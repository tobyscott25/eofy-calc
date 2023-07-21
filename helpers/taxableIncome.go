package helpers

func CalcTaxableIncome(salary int, salarySacrificePercentage int) int {
	return salary - (salary * salarySacrificePercentage / 100)
}
