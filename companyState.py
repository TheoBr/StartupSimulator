import sys, os 

class CompanyState:

	funding = 0
	day = 0
	employees = []
	companyName = ""
	companyBio = ""
	features = []

	def __init__(self, companyName):
		self.companyName = companyName
		companyBio = self.generateBio(companyName)

	def generateBio(self, companyName):
		# TODO
		return "Tinder for Dogs"

	def addEmployee(self, employee):
		if isinstance(employee, Employee):
			self.employees.append(employee)
		else:
			print "ERROR: Make sure you are adding Employees"

	def tickTime(self):
		self.day+=1
		# TODO: 
		# - Random chance of event
		# - Deduct salaries if mod(365) == 0
		# - Percentage development of feature

class Employee:
	salary = 0
	name = ""

	def __init__(self, name):
		self.name = name

		# TODO: Function that takes in time and determines salary
		salary = 0

def main():
	name = raw_input("Please enter a name for your new startup")
	initial_state = CompanyState(name)


if __name__ == '__main__':
	main()