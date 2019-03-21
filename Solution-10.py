# Solution to Problem 10
# Eoin Dowling 17-Mar-2019


# Commands for matplolib from lectures week 9, code adapted from: https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt
import numpy as np

# First function x =(0,1,2,3,4) created in array to facilitate 2^x in final graph
x = np.array([0,1,2,3,4])

plt.plot(x)
plt.ylabel('x in range [0,4]')
plt.show()

# Take each item in list and square, code adapted from: https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717
xx = np.array([i**2 for i in x])

plt.plot(xx)
plt.ylabel('x^2 in range[0,4]')
plt.show()

# Created to allow for calculation of 2^x
l = np.array([2,2,2,2,2])
# Creating arrays for x and l allowed for there points to be powered for final graph.
xxx = l**x

plt.plot(xxx)
plt.ylabel('2^x in range[0,4]')
plt.show()