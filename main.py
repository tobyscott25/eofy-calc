import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls() # Clear the screen

annual_salary = float(input("Your annual salary (e.g. \"50\" = $50,000): ")) * 1000

if annual_salary > 90000:
	# Asked for the Medicare Levy Surcharge
	private_health_cover = bool(input("Do you have private health cover? (y/n): "))

salary_sacrifice = float(input("What percentage of that do you salary sacrifice? (%): "))
hecs_debt = bool(input("Do you have a HECS/FEE-Help debt? (true/false): "))

# Are you a senior or pensioner? (y/n):
# Were you eligible for the seniors and pensioners tax offset (SAPTO)? (y/n):
sapto = False

# Do you have a spouse (married or de facto)? (y/n):
#  Did you have a spouse (married or de facto) on 30 June of the selected income year?
single = True

# Number of dependants:
dependants_count = 0


bills = float(input("Monthly cost on bills (e.g. rent/mortgage, utility bills, rates etc) ($): ")) * 12
necessities = float(input("Estimated monthly cost on general necessities (e.g. groceries, hygiene products, doctor/dentist appointments, etc) ($): ")) * 12
luxuries = float(input("Estimated monthly cost on luxuries (e.g. streaming subscriptions, eating out, etc) ($): ")) * 12



taxable_income = annual_salary * (1 - salary_sacrifice / 100)

if taxable_income <= 18200: # Up to $18,200
	tax = 0

elif taxable_income <= 45000: # Up to $45,000

	# Tax every dollar after $18,200 at 19%
	tax_rate = 0.19
	amount_to_tax = taxable_income - 18200
	tax = amount_to_tax * tax_rate

	# Add the tax from the previous bracket(s)
	tax = tax + 0

elif taxable_income <= 120000: # Up to $120,000

	# Tax every dollar after $45,000 at 32.5%
	tax_rate = 0.325
	amount_to_tax = taxable_income - 45000
	tax = amount_to_tax * tax_rate

	# Add the tax from the previous bracket(s)
	tax = tax + 5092

elif taxable_income <= 180000: # Up to $180,000

	# Tax every dollar after $120,000 at 37%
	tax_rate = 0.37
	amount_to_tax = taxable_income - 120000
	tax = amount_to_tax * tax_rate

	# Add the tax from the previous bracket(s)
	tax = tax + 29467

else: # Over $180,000

	# Tax every dollar after $180,000 at 45%
	tax_rate = 0.45
	amount_to_tax = taxable_income - 180000
	tax = amount_to_tax * tax_rate

	# Add the tax from the previous bracket(s)
	tax = tax + 51667


# Medicare Levy. !! Currently only supports Standard Medicare Levy and ML Exemption. Not MLS or ML Reduction. !!
ml = taxable_income * 0.02
if (single and taxable_income <= 23365):
	ml = 0
# if (single and taxable_income <= 29207):
# 	ml = 0
mls = 0



if hecs_debt:
	if annual_salary <= 48360: # Up to 48,360
		hecs_repayment_rate = 0
	elif annual_salary <= 55836: # Up to 55,836
		hecs_repayment_rate = 0.01
	elif annual_salary <= 59186: # Up to 59,186
		hecs_repayment_rate = 0.02
	elif annual_salary <= 62738: # Up to 62,738
		hecs_repayment_rate = 0.025
	elif annual_salary <= 66502: # Up to 66,502
		hecs_repayment_rate = 0.03
	elif annual_salary <= 70492: # Up to 70,492
		hecs_repayment_rate = 0.035
	elif annual_salary <= 74722: # Up to 74,722
		hecs_repayment_rate = 0.04
	elif annual_salary <= 79206: # Up to 79,206
		hecs_repayment_rate = 0.045
	elif annual_salary <= 83958: # Up to 83,958
		hecs_repayment_rate = 0.05
	elif annual_salary <= 88996: # Up to 88,996
		hecs_repayment_rate = 0.055
	elif annual_salary <= 94336: # Up to 94,336
		hecs_repayment_rate = 0.06
	elif annual_salary <= 99996: # Up to 99,996
		hecs_repayment_rate = 0.065
	elif annual_salary <= 105996: # Up to 105,996
		hecs_repayment_rate = 0.07
	elif annual_salary <= 112335: # Up to 112,335
		hecs_repayment_rate = 0.075
	elif annual_salary <= 119097: # Up to 119,097
		hecs_repayment_rate = 0.08
	elif annual_salary <= 126243: # Up to 126,243
		hecs_repayment_rate = 0.085
	elif annual_salary <= 133818: # Up to 133,818
		hecs_repayment_rate = 0.09
	elif annual_salary <= 141847: # Up to 141,847
		hecs_repayment_rate = 0.095
	else: # Above 141,847
		hecs_repayment_rate = 0.1
else:
	hecs_repayment_rate = 0

hecs_repayment = annual_salary * hecs_repayment_rate


def print_report():

	cls() # Clear the screen

	print('============================================================')
	print('\n')
	print(f'Gross annual salary: ${annual_salary}')
	print(f'Salary sacrifice: {salary_sacrifice}% (-${annual_salary - taxable_income})')
	print(f'Taxable income: ${taxable_income}')
	print('\n')
	print(f'PAYG income tax: -${tax}')
	print(f'Medicare Levy: -${ml}')
	if mls > 0:
		print(f'Medicare Levy Surcharge: -${mls}')
	
	if hecs_debt:
		print(f'HECS Repayment: {hecs_repayment_rate * 100}% (-${hecs_repayment})')
		print('\n')
		print(f'Total going to ATO: -${ml + mls + tax + hecs_repayment})')

	
	print(f'Leaving you with ${taxable_income - tax - hecs_repayment - ml - mls}')
	print('\n')
	print(f'Bills: -${bills}')
	print(f'General necessities: -${necessities}')
	print(f'Luxuries: -${luxuries}')
	print('\n')
	print(f'Leaving you with ${taxable_income - tax - bills - necessities - luxuries - hecs_repayment - ml - mls}')
	print('\n')
	print('============================================================')
	print('\n')

print_report()