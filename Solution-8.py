# Solution to Problem 8
# Eoin Dowling 12-Mar-2019

import datetime

time =  datetime.datetime.now()
# Needed day as str as concatenate will not join int and str. day returns value as int.
day = str(datetime.datetime.now().day)

# Created if statement to determine suffix for date i.e th st rd nd
if time.day == 1 or time.day == 21 or time.day == 31:
	suffix = 'st'
elif time.day == 2 or time.day == 22:
	suffix = 'nd'
elif time.day == 3 or time.day == 23:
	suffix = 'rd'
else: suffix = 'th'

# Used to join str.day with suffix
daysuffix = day + suffix
# Removed old code as discovered cleaner way to format using code from: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
timeformat = time.strftime("%A, %B")
# Formatted times using table located here: https://docs.python.org/3/library/time.html
timeformat2 = time.strftime("%Y at %I:%M")
# Created to get suffix working for hour i.e. pm/am
if time.hour >=12:
	suffixhour = 'pm'
else: suffixhour = 'am'

timeformat2suffix = timeformat2 + suffixhour

print(timeformat,daysuffix,timeformat2suffix)