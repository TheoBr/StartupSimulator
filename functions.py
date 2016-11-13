import random

def generateSalary(time): 
# Generate salary given time 
	base = 70000
	modifier = 1000
	percent = 20
	luck = random.random
	return (base + (modifier * percent * luck)) 

def generateInvestmentOffer(time):
	base = 1000000
	modifier = 10000
	percent = 20
	luck = random.random
	return (base + (modifier * percent * luck)) 

def generateBio(companyName):
# TODO generate bio given company name
	return "Shopify for florists"