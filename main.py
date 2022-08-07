import os
from Profile import Profile

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Clear the screen on fresh run
cls()


def input_val_loop(data_type: type, prompt: str):
	while True:
		try:
			if data_type == int:
				return int(input(prompt))
			elif data_type == float:
				return float(input(prompt))
			elif data_type == bool:
				return bool(input(prompt))
			elif data_type == str:
				return str(input(prompt))
			else:
				raise ValueError('Invalid input type.')
		except ValueError:
			print('Please check the data type you used.')
			continue



# PREPARE THE PROFILE

annual_salary = input_val_loop(float, 'Your annual salary (e.g. "50" = $50,000 or "60.53" = $60,530): ') * 1000

if annual_salary > 90000:
	# For Medicare Levy Surcharge
	private_health_cover = input_val_loop(bool, 'Do you have private health cover? (true/false): ')
else:
	private_health_cover = False # Irrelevant when salary is less than $90000 so may as well be false

salary_sacrifice = input_val_loop(float, "What percentage of that do you salary sacrifice? (%): ")
hecs_debt = input_val_loop(bool, "Do you have a HECS/FEE-Help debt? (true/false): ")
sapto = False # Were you eligible for the seniors and pensioners tax offset (SAPTO)? (true/false):
single = True # Do you have a spouse (married or de facto)? (true/false):
dependants = 0 # Number of dependants:
# Monthly cost on bills
bills = input_val_loop(float, "Monthly cost on bills (e.g. rent/mortgage, utility bills, rates etc) ($): ") * 12
# Monthly cost on general necessities
necessities = input_val_loop(float, "Estimated monthly cost on general necessities (e.g. groceries, hygiene products, doctor/dentist appointments, etc) ($): ") * 12
# Monthly cost on luxuries
luxuries = input_val_loop(float, "Estimated monthly cost on luxuries (e.g. streaming subscriptions, eating out, etc) ($): ") * 12

freshprof = Profile(annual_salary, salary_sacrifice, private_health_cover, hecs_debt, bills, necessities, luxuries)

# FINISH PROFILE

freshprof.generate_report()