
annual_salary = float(input("Your annual salary? ($x,000): ")) * 1000
salary_sacrifice = float(input("What percentage, are you salary sacrificing before tax? (%): "))
taxable_income = annual_salary * (1 - salary_sacrifice / 100)

def print_report():

	print('\n')
	print('============================================================')
	print(f'Gross annual salary: ${annual_salary}')
	print('\n')
	print(f'Salary sacrifice (pre-tax): {salary_sacrifice}% (${annual_salary - taxable_income})')
	print(f'Taxable income: ${taxable_income}')
	print('============================================================')
	print('\n')

print_report()