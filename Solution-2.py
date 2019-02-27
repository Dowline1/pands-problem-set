# Solution to Problem 2
# Eoin Dowling 26-Feb-2019

# Adapted from lecture on it is Sunday week 2 Programming & Scripting 

import datetime

# Updated or statement as before did not work as did not specify all statement alternative of or.
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3 :
  print("Yes, Today does begin with a T.")
else:
  print("No, Today does not begin with T.")

x = datetime.datetime.today().weekday()

print(x) 


