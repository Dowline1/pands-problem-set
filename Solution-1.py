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
start = 10
ans = 1

while start > 1:
  ans = ans * start
  start = start - 1

print (ans)