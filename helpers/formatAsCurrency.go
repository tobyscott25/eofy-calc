package helpers

import (
	"fmt"
	"strings"
)

func FormatAsCurrency(amount float64) string {
	intPart, decPart := int(amount), int((amount-float64(int(amount)))*100)
	var parts []string

	for intPart >= 1000 {
		parts = append(parts, fmt.Sprintf("%03d", intPart%1000))
		intPart /= 1000
	}

	parts = append(parts, fmt.Sprintf("%d", intPart))

	// Reverse and join
	for i, j := 0, len(parts)-1; i < j; i, j = i+1, j-1 {
		parts[i], parts[j] = parts[j], parts[i]
	}

	return fmt.Sprintf("$%s.%02d", strings.Join(parts, ","), decPart)
}
