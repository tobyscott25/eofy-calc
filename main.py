import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls() # Clear the screen

annual_salary = float(input("Your annual salary (e.g. \"50\" = $50,000): ")) * 1000
salary_sacrifice = float(input("What percentage of that do you salary sacrifice? (%): "))

bills = float(input("Monthly cost on bills (e.g. rent/mortgage, utility bills, rates etc) ($): ")) * 12
necessities = float(input("Estimated monthly cost on general necessities (e.g. groceries, hygiene products, doctor/dentist appointments, etc) ($): ")) * 12
luxuries = float(input("Estimated monthly cost on luxuries (e.g. streaming subscriptions, eating out, etc) ($): ")) * 12



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




def print_report():

	cls() # Clear the screen

	print('\n')
	print('============================================================')
	print(f'ANNUAL LIFE RECEIPT - Annual salary: ${annual_salary}')
	print('============================================================')
	# print(f'Gross annual salary: ${annual_salary}')
	print('\n')
	print(f'Salary sacrifice: {salary_sacrifice}% (-${annual_salary - taxable_income})')
	print(f'Taxable income: ${taxable_income}')
	print(f'Tax: -${tax}')
	print('\n')
	print(f'Leaving you with ${taxable_income - tax}')
	print('\n')
	print(f'Bills: -${bills}')
	print(f'General necessities: -${necessities}')
	print(f'Luxuries: -${luxuries}')
	print('\n')
	print(f'Leaving you with ${taxable_income - tax - bills - necessities - luxuries}')
	print('\n')
	print('============================================================')
	print('\n')

print_report()