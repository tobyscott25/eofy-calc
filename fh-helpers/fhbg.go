package fhhelpers

func IsFHBGEligible(salary float64) bool {
	return salary <= 128000 // Eligibility based on salary less than or equal to $128,000
}
