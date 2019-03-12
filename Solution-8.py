# Solution to Problem 8
# Eoin Dowling 12-Mar-2019

import datetime

# Adapting code from Solution-2.py to give day of week as word.
if datetime.datetime.today().weekday() == 0:
  day = "Monday"
elif datetime.datetime.today().weekday() == 1:
  day = "Tuesday"
elif datetime.datetime.today().weekday() == 2:
  day = "Wednesday"
elif datetime.datetime.today().weekday() == 3:
  day = "Thursday"
elif datetime.datetime.today().weekday() == 4:
  day = "Friday"
elif datetime.datetime.today().weekday() == 5:
  day = "Saturday"
elif datetime.datetime.today().weekday() == 6:
  day = "Sunday"

print(datetime.datetime.now())
print(day)