import unittest
from companyState import *

class companyStateTest(unittest.TestCase):
	"""Tests for CompanyState.py"""

	def test(self):
		company = CompanyState("NewCompany")	
		"""Asserts company was made correct"""
		self.assertEqual(company.companyName, "NewCompany")
		tempEmployee = Employee("Susan")
		"""Asserts employee was made correct"""
		self.assertEqual(tempEmployee.name, "Susan")
		company.addEmployee(tempEmployee)
		"""Asserts employee was added to company correct"""
		self.assertEqual(company.employees[0].name, "Susan")

if __name__ == '__main__':
    unittest.main()