"""
Input: A cash amount, in dollars and cents.

Process: Divide the total by each denomination in order to determine how much of each type of denomination to return.

Output: The total number of each type of bill and coin to return for change.
"""

def convert2Change():
	totalCurrency = eval(input("Enter in the total amount of money you have: $"))
	
	numHundreds = totalCurrency // 100
	print("Give back", int(numHundreds), "$100 bills")
	totalCurrency = totalCurrency % 100
	
	numFifties = totalCurrency // 50
	print("Give back", int(numFifties), "$50 bills")
	totalCurrency = totalCurrency % 50
	
	numTwenties = totalCurrency // 20
	print("Give back", int(numTwenties), "$20 bills")
	totalCurrency = totalCurrency % 20
	
	numTens = totalCurrency // 10
	print("Give back", int(numTens), "$10 bills")
	totalCurrency = totalCurrency % 10
	
	numFives = totalCurrency // 5
	print("Give back", int(numFives), "$5 bills")
	totalCurrency = totalCurrency % 5
	
	numOnes = totalCurrency
	print("Give back", int(numOnes), "$1 bills")
	totalCurrency = totalCurrency % 1

	numQuarters = totalCurrency // 0.25
	print("Give back", int(numQuarters), "quarters")
	totalCurrency = totalCurrency % 0.25
	
	numDimes = totalCurrency // 0.10
	print("Give back", int(numDimes), "dimes")
	totalCurrency = totalCurrency % 0.10
	
	numNickels = totalCurrency // 0.05
	print("Give back", int(numNickels), "nickels")
	totalCurrency = totalCurrency % 0.05
	
	numPennies = totalCurrency // 0.01
	print("Give back", numPennies, "pennies")
	
	
def main():
	convert2Change()
	
main()