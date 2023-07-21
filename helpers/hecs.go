package helpers

func CalcHecsHelpRepaymentRate(salary int) float64 {
	switch {
	case salary <= 48360: // Up to $48,360
		return 0
	case salary <= 55836: // Up to $55,836
		return 0.01
	case salary <= 59186: // Up to $59,186
		return 0.02
	case salary <= 62738: // Up to $62,738
		return 0.025
	case salary <= 66502: // Up to $66,502
		return 0.03
	case salary <= 70492: // Up to $70,492
		return 0.035
	case salary <= 74722: // Up to $74,722
		return 0.04
	case salary <= 79206: // Up to $79,206
		return 0.045
	case salary <= 83958: // Up to $83,958
		return 0.05
	case salary <= 88996: // Up to $88,996
		return 0.055
	case salary <= 94336: // Up to $94,336
		return 0.06
	case salary <= 99996: // Up to $99,996
		return 0.065
	case salary <= 105996: // Up to $105,996
		return 0.07
	case salary <= 112335: // Up to $112,335
		return 0.075
	case salary <= 119097: // Up to $119,097
		return 0.08
	case salary <= 126243: // Up to $126,243
		return 0.085
	case salary <= 133818: // Up to $133,818
		return 0.09
	case salary <= 141847: // Up to $141,847
		return 0.095
	default: // Above $141,847
		return 0.1
	}
}
