# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 6

""" 
 Define a procedure, factorial, 
 that takes a natural number as its input, and
 returns the number of ways to arrange the input number of items.
""" 

# recursive procedure
def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

# test Code
print factorial(0)
print factorial(5)
print factorial(10)