# Solution to Problem 9
# Eoin Dowling 12-Mar-2019

# Assumptions output to begin from line 1 inclusive
# Using module itertools as identifeied and used from source: https://stackoverflow.com/questions/36487709/how-to-print-every-third-or-n-th-line-from-file-in-python?rq=1
from itertools import islice

# Used to prompt user to input name of txt file to read e.g. provided is as per below.
text = input("Please enter the name of a file in this location. e.g. road-not-taken.txt ")

# Code adapted from previous weeks lecture and combined with code from here: https://stackoverflow.com/questions/36487709/how-to-print-every-third-or-n-th-line-from-file-in-python?rq=1
with open(text) as f:
	# islice works by returning as per parametres below i.e. (variable that was opened, start line, line to stop at, step by which to output in this example every second line.)
  for l in islice(f, 0, None, 2):
      print(l)
