import sys, os, companyState, random

from functions import *

# File for all Event functions
events = dict()


def nigerianPrinceInvestsInheritance(state):
	investment = 1000 * state.day * random.random()
	state.funding += investment
	return state

def suedByPatentTrollForUsingPrinter(state):
	settlement = (.25 * state.funding) * (state.day * random.random())
	state.funding -= settlement
	return state


def secureWorldSeriesFundingFromMLB(state):
	investment = (.75 * state.funding) * (state.day * random.random())
	state.funding += investment
	return state


def hireOverworkedCollegeKidFromHackathon(state):
	names = ["Theo", "Courtney", "Abigail", "Katie", "Robert"]
	salary = generateSalary(state.day)

	newHire = companyState.Employee(random.choice(names), salary)
	state.addEmployee(newHire)
	return state








# Return dictionary of all events
def getEvents():
	events['nigerianPrinceInvestsInheritance'] = nigerianPrinceInvestsInheritance
	events['suedByPatentTrollForUsingPrinter'] = suedByPatentTrollForUsingPrinter
	events['secureWorldSeriesFundingFromMLB'] = secureWorldSeriesFundingFromMLB

	return events