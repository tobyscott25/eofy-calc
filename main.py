
annual_salary = float(input("Your annual salary? ($x,000 e.g. \"50\" = 50,000): ")) * 1000
salary_sacrifice = float(input("What percentage, are you salary sacrificing before tax? (%): "))
taxable_income = annual_salary * (1 - salary_sacrifice / 100)



if taxable_income <= 18200:
	# Tax-free threshold
	tax = 0
elif taxable_income >= 18201 and taxable_income <= 45000:
	tax_rate = 0.19
	# Tax every dollar after $18,200 at 19%
	tax = (taxable_income - 18200) * tax_rate
	# Add the tax from the previous bracket(s)
	tax = tax + 0
elif taxable_income >= 45001 and taxable_income <= 120000:
	tax_rate = 0.325
	# Tax every dollar after $45,000 at 32.5%
	tax = (taxable_income - 45000) * tax_rate
	# Add the tax from the previous bracket(s)
	tax = tax + 5092
elif taxable_income >= 120001 and taxable_income <= 180000:
	tax_rate = 0.37
	# Tax every dollar after $120,000 at 37%
	tax = (taxable_income - 120000) * tax_rate
	# Add the tax from the previous bracket(s)
	tax = tax + 29467
else:
	tax_rate = 0.45
	# Tax every dollar after $180,000 at 45%
	tax = (taxable_income - 180000) * tax_rate
	# Add the tax from the previous bracket(s)
	tax = tax + 51667

remainder = taxable_income - tax



def print_report():

	print('\n')
	print('============================================================')
	print(f'Gross annual salary: ${annual_salary}')
	print('\n')
	print(f'Salary sacrifice (pre-tax): {salary_sacrifice}% (${annual_salary - taxable_income})')
	print(f'Taxable income: ${taxable_income}')
	print('\n')
	print(f'You pay ${tax}, leaving you with ${remainder}')
	print('============================================================')
	print('\n')

print_report()