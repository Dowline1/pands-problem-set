# Solution to Problem 5
# Eoin Dowling 28-Feb-2019

# Starting program input from code created in solution 1 and adapting as necessary.
while True:
	try:
		start = int(input("Please enter a positive integer "))
		assert(start>0)
		break
	except:
		print("You entered a number less than 1 or a non numeric character, please try again.")

# Counter to determine number of times modulo of start to 2 is = 0
count = 0
# Needed diviser to keep track of what to divide start by 
diviser = start

# Adapting code that was used in Solution 1.
# Prime number is a natural number divisble evenly by itself and 1 i.e. modulo must = 0. Note: 1 is not a primes number as only has one divisor (Prime must = 2 Divisors):https://brilliant.org/wiki/is-1-prime/
while   diviser > 1:
    if (start % diviser == 0):
        count = count + 1
        diviser = diviser - 1
    # Added elif as program was getting stuck in infinite loop as program did not know what to do if start%diviser was not = 0    
    elif (start % diviser != 0):
        diviser = diviser - 1

# Formatted output of programme to make more sense.
if (count == 1):
    print(start,'is a Prime Number.')

else:
    print(start,'is not a Prime Number.')