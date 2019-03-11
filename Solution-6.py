# Solution to Problem 6
# Eoin Dowling 11-Mar-2019

# Assumptions: Instructions from question on assignement states program outputs every second word, however example below question gives "The brown jumps the dog" This would mean to remove every second word. My understandin is to output every second word from word 2 i.e."quick fox over lazy"

# Starting program input from code created in solution 1 and adapting as necessary. Stores input as start.
start = input("Please enter a sentence ")
# Below splits string into list of words seperated by white space from input. Source of code: http://www.pitt.edu/~naraehan/python3/split_join.html
startsplit = start.split()
# Below takes the list of words and from the second character returns every second word in list. Source of code: https://stackoverflow.com/questions/8865878/skipping-every-other-element-after-the-first/8865905
# Split works like this: [index of start point(i.e first word per below code): index of endpoint(i.e no end point per below code): steps between(i.e every second word from start point)].
startslice = startsplit[1::2]

print (startsplit)
print (startslice)