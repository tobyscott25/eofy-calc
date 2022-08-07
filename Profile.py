class Profile:
	def __init__(self, salary: float, percentage_sacrificed: float, private_health: bool, hecs_debt: bool, monthly_bills: float, monthly_necessities: float, monthly_luxuries: float):
		
		float: self.salary 					= salary
		float: self.percentage_sacrificed 	= percentage_sacrificed
		bool: self.private_health 			= private_health
		bool: self.hecs_debt 				= hecs_debt

		float: self.monthly_bills 			= monthly_bills
		float: self.monthly_necessities 	= monthly_necessities
		float: self.monthly_luxuries 		= monthly_luxuries

		float: self.taxable_income 			= salary * (1 - percentage_sacrificed / 100)


		# Currently hardcoded defaults, yet to be made variable:

		bool: self.sapto_eligible 			= False
		bool: self.single 					= True
		int: self.dependants 				= 0

