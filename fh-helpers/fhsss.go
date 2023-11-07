package fhhelpers

func CalculateFHSSS(salary float64) float64 {
	if salary >= 15000 { // Assuming a threshold for salary sacrifice
		return 15000 // Maximum of $15,000 can be salary sacrificed each year
	}
	return 0
}
