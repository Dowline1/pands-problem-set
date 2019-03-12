# Solution to Problem 8
# Eoin Dowling 12-Mar-2019

import datetime

time =  datetime.datetime.now()
# Needed day as str as concatenate will not join int and str. day returns value as int.
day = str(datetime.datetime.now().day)

# Created if statement to determine suffix for date i.e th st rd nd
if time.day == 12:
	suffix = 'th'

# Used to join str.day with suffix
daysuffix = day + suffix
# Removed old code as discovered cleaner way to format using code from: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
timeformat = time.strftime("%A, %B")

print(timeformat,daysuffix)