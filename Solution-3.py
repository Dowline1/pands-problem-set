# Solution to Problem 3
# Eoin Dowling 27-Feb-2019

# My Assumption of between in problem 3 is 1001....9999 inclusive. 
Start = 1000
End = 10000

# Switched to for statement to so that could use range function, code adapted from: https://www.sanfoundry.com/python-program-print-numbers-range-divisible-given-number/
# Range includes all number between 2 points ie not including two numbers, lists can also be used
for i in range(Start, End+1):
	  #as described in previous lectures modulo (%) returns remainder of division of 2 numbers eg 2%6 = 2 as 2 is remainder as 6 does not divide into 2.
		if(i%6==0):
			print(i)

