# Solution to Problem 2
# Eoin Dowling 26-Feb-2019

# Adapted from lecture on it is Sunday week 2 Programming & Scripting 

import datetime

# Updated or statement as before did not work as did not specify all statement alternative of or.
# Correct use of or adapted from: https://www.w3schools.com/python/python_conditions.asp
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3 :
  print("Yes, Today does begin with a T.")
else:
  print("No, Today does not begin with T.")

# Adding day counter to inform how many days until it will be a day begining with T.
if datetime.datetime.today().weekday() == 0 or datetime.datetime.today().weekday() == 2:
  print("Tomorrow will begin with a T.")
elif datetime.datetime.today().weekday() == 4:
  print("Four more sleeps to go.")
elif datetime.datetime.today().weekday() == 5:
  print ("Three more sleeps to go.")
elif datetime.datetime.today().weekday() == 6:
  print("Two more sleeps to go.")


