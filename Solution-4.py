# Solution to Problem 4
# Eoin Dowling 27-Feb-2019

# Starting program input from code created in solution 1 and adapting as necessary.
while True:
	try:
		start = int(input("Please enter a positive integer "))
		assert(start>0)
		break
	except:
		print("You entered a number less than 1 or a non numeric character, please try again.")

# Print moved here to show initial start value and prevent infinite loop.
print (start)
# Adapted code from Solution 3 using modulo to determine what way calculation is performed.
while start > 1:
	if start%2 == 0:
		# Was getting infinite loop as had forgotten to update start after calculation.
		start = int(start/2)
		print(start)
	else:
		# Added int when updating start to remove decimals in print results.
		start = int((start*3)+1)
		print(start)
