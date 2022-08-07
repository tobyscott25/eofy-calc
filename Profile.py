import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
	

class Profile:
	def __init__(self, salary: float, percentage_sacrificed: float, private_health: bool, hecs_debt: bool, bills: float, necessities: float, luxuries: float):
		
		self.salary 					= salary
		self.percentage_sacrificed 		= percentage_sacrificed
		self.private_health 			= private_health
		self.hecs_debt 					= hecs_debt

		self.bills 						= bills
		self.necessities 				= necessities
		self.luxuries 					= luxuries

		# Calculated from above answers
		# self.taxable_income 			= self.salary * (1 - self.percentage_sacrificed / 100)

		# Currently hardcoded defaults, yet to be made variable:
		self.sapto_eligible 			= False
		self.single 					= True
		self.dependants 				= 0


	def calc_taxable_income(self):
		return self.salary * (1 - self.percentage_sacrificed / 100)

	def calc_income_tax(self):

		if self.calc_taxable_income() <= 18200: # Up to $18,200
			tax = 0

		elif self.calc_taxable_income() <= 45000: # Up to $45,000

			# Tax every dollar after $18,200 at 19%
			amount_to_tax = self.calc_taxable_income() - 18200
			tax = amount_to_tax * 0.19

			# Add the tax from the previous bracket(s)
			tax = tax + 0

		elif self.calc_taxable_income() <= 120000: # Up to $120,000

			# Tax every dollar after $45,000 at 32.5%
			amount_to_tax = self.calc_taxable_income() - 45000
			tax = amount_to_tax * 0.325

			# Add the tax from the previous bracket(s)
			tax = tax + 5092

		elif self.calc_taxable_income() <= 180000: # Up to $180,000

			# Tax every dollar after $120,000 at 37%
			amount_to_tax = self.calc_taxable_income() - 120000
			tax = amount_to_tax * 0.37

			# Add the tax from the previous bracket(s)
			tax = tax + 29467

		else: # Over $180,000

			# Tax every dollar after $180,000 at 45%
			amount_to_tax = self.calc_taxable_income() - 180000
			tax = amount_to_tax * 0.45

			# Add the tax from the previous bracket(s)
			tax = tax + 51667
		
		return tax

	def calc_hecs_repayment_rate(self):

		if self.hecs_debt:
			if self.salary <= 48360: # Up to 48,360
				hecs_repayment_rate = 0
			elif self.salary <= 55836: # Up to 55,836
				hecs_repayment_rate = 0.01
			elif self.salary <= 59186: # Up to 59,186
				hecs_repayment_rate = 0.02
			elif self.salary <= 62738: # Up to 62,738
				hecs_repayment_rate = 0.025
			elif self.salary <= 66502: # Up to 66,502
				hecs_repayment_rate = 0.03
			elif self.salary <= 70492: # Up to 70,492
				hecs_repayment_rate = 0.035
			elif self.salary <= 74722: # Up to 74,722
				hecs_repayment_rate = 0.04
			elif self.salary <= 79206: # Up to 79,206
				hecs_repayment_rate = 0.045
			elif self.salary <= 83958: # Up to 83,958
				hecs_repayment_rate = 0.05
			elif self.salary <= 88996: # Up to 88,996
				hecs_repayment_rate = 0.055
			elif self.salary <= 94336: # Up to 94,336
				hecs_repayment_rate = 0.06
			elif self.salary <= 99996: # Up to 99,996
				hecs_repayment_rate = 0.065
			elif self.salary <= 105996: # Up to 105,996
				hecs_repayment_rate = 0.07
			elif self.salary <= 112335: # Up to 112,335
				hecs_repayment_rate = 0.075
			elif self.salary <= 119097: # Up to 119,097
				hecs_repayment_rate = 0.08
			elif self.salary <= 126243: # Up to 126,243
				hecs_repayment_rate = 0.085
			elif self.salary <= 133818: # Up to 133,818
				hecs_repayment_rate = 0.09
			elif self.salary <= 141847: # Up to 141,847
				hecs_repayment_rate = 0.095
			else: # Above 141,847
				hecs_repayment_rate = 0.1
		else:
			hecs_repayment_rate = 0

		return hecs_repayment_rate

	def calc_hecs_repayment_amount(self):
		return self.salary * self.calc_hecs_repayment_rate()

	# Doesn't calculate ML Surcharge or ML Reduction yet
	def calc_medicare_levy(self):
		
		# Standard Medicare Levy
		medicare_levy = self.calc_taxable_income() * 0.02

		# Medicare Levy Exemption
		if (self.single and self.calc_taxable_income() <= 23365):
			medicare_levy = 0

		return medicare_levy

	def generate_report(self):

		cls() # Clear the screen

		print('============================================================')
		print('\n')
		print(f'Gross annual salary: ${self.salary}')
		print(f'Salary sacrifice: {self.percentage_sacrificed}% (-${self.salary - self.calc_taxable_income()})')
		print(f'Taxable income: ${self.calc_taxable_income()}')
		print('\n')
		print(f'PAYG income tax: -${self.calc_income_tax()}')
		print(f'Medicare Levy: -${self.calc_medicare_levy()}')
		# if medicare_levy_surcharge > 0:
		# 	print(f'Medicare Levy Surcharge: -${medicare_levy_surcharge}')
		
		if self.hecs_debt:
			print(f'HECS Repayment: {self.calc_hecs_repayment_rate() * 100}% (-${self.calc_hecs_repayment_amount()})')
			print('\n')
			print(f'Total going to ATO: -${self.calc_medicare_levy() + self.calc_income_tax() + self.calc_hecs_repayment_amount()})')

		
		print(f'Leaving you with ${self.calc_taxable_income() - self.calc_income_tax() - self.calc_hecs_repayment_amount() - self.calc_medicare_levy()}')
		print('\n')
		print(f'Bills: -${self.bills}')
		print(f'General necessities: -${self.necessities}')
		print(f'Luxuries: -${self.luxuries}')
		print('\n')
		print(f'Leaving you with ${self.calc_taxable_income() - self.calc_income_tax() - self.calc_hecs_repayment_amount() - self.calc_medicare_levy() - self.bills - self.necessities - self.luxuries}')
		print('\n')
		print('============================================================')
		print('\n')