package fhhelpers

func CalculateStampDuty(cost float64, propertyType string, firstHome bool) float64 {
	var stampDuty float64

	if firstHome {
		if cost <= 600000 {
			// Full exemption for first homes up to $600,000
			stampDuty = 0
		} else if cost > 600000 && cost <= 750000 {
			// Concession on a sliding scale for first homes between $600,001 and $750,000
			// Specific calculation will vary based on the cost
			stampDuty = (cost - 600000) * 0.05 // Simplified sliding scale calculation
		} else {
			// Standard rates apply for first homes above $750,000
			stampDuty = cost * 0.05 // Assuming a flat 5% for simplicity
		}
	} else {
		// Calculation for non-first-home buyers goes here
		stampDuty = cost * 0.05 // Placeholder calculation
	}

	return stampDuty
}
