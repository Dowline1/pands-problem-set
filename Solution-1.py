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



# Adding input screen source for input (https://www.w3schools.com/python/ref_func_input.asp)

# Updated material type for start to int (source python tutorial) as before was giving error due to inputs being a string as default

ans = 1

# code adapted from below link which prevents numbers less than 0 and non numeric characters being entered.
# Adapted from: https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python
 
while True:
  # Try Statement used with except statement below controls what happens with code, in this case if input > 0 break terminates the while loop and code continues.
  try:
    start = int(input("Please enter a positive Integer "))

# Assert is a boolean expression and checks in this case that input is > 0(True) or input < 0 (False), if False assertion error given.
    assert (start > 0)
    break

# In this case if input is < 0 or non numeric character entered except executes (assert error when False). 
# Except is an exception handler, when break is not executed in code below, except initiates prints the text and begins while again until criteria met.

  except:
    print("You entered a number less than 1 or a non numeric character, please try again.")


# As highlighted during lecture below is line of thought to simplify code
# Keep multiplying ans by start while start greater than 1
# Only 2 things reqiuired to workout factorial (number to calculate and 1 ie always stop at 1)
# i not required as factorial multiplaction always ends at 1

# Tracks number inputted
begin = start
start = int(start)

while start > 1:
  ans = ans + start
  start = start - 1

# Formats output in a way that makes sense.
print ('The sum of all numbers between',begin,'and 1 inclusive is',ans,'.')