package fhhelpers

func CalculateGrant(cost float64, propertyType string, firstHome bool) float64 {
	var grant float64

	// Assuming this grant is only available for first homes that are new and cost $750,000 or less
	if firstHome && propertyType == "New" && cost <= 750000 {
		grant = 10000 // Grant amount for eligible new first homes
	} else {
		grant = 0 // No grant for homes that don't meet the criteria
	}

	return grant
}
