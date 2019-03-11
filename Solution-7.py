# Solution to Problem 7
# Eoin Dowling 11-Mar-2019

# Imports Pythons math module
import math

# Starting program input from code created in solution 1 and adapting as necessary.
while True:
	try:
		start = float(input("Please enter a positive floating point number "))
		assert(start>0.0)
		break
	except:
		print("You entered a number less than 0 or a non numeric character, please try again.")

# Below calculates square root of number inputed. Source: https://www.tutorialspoint.com/python3/number_sqrt.htm
ans = math.sqrt(start)

# Round used to round result to 1 decimal place. Source of code: https://docs.python.org/3/library/functions.html?highlight=round#round
ans = round(ans,1)

print(ans)