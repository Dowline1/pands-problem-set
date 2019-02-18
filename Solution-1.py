#Solution to Problem 1

# Eoin Dowling 01-Feb-2019 (Initial code from Lecture 2) 
# Calculate the factorial of a number

# Ian program
#start = 10
#ans = 1
#i = 1

#while i <= start:
#  ans = ans * i
#  i = i + 1

#print (ans)

# As highlighted during lecture below is line of thought to simplify code
# Keep multiplying ans by start while start greater than 1
# Only 2 things reqiuired to workout factorial (number to calculate and 1 ie always stop at 1)
# i not required as factorial multiplaction always ends at 1

# Adding input screen source for input (https://www.w3schools.com/python/ref_func_input.asp)

# Updated material type for start to int (source python tutorial) as before was giving error due to inputs being a string as default

ans = 1

# code adapyed from below link which prevents numbers less than 0 and non numeric characters being entered.
# https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python
while True:
  try:
    start = int(input("Please enter a positive Integer "))
    assert (start > 0)
    break
  except:
    print("You entered a number less than 1 or a non numeric character, please try again.")


start = int(start)

while start > 1:
  ans = ans + start
  start = start - 1

print (ans)