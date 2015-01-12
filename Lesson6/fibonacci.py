# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 6

# Define a faster fibonacci procedure that will enable us to 
# computer fibonacci(36).

# define the iterative procedure
def fibonacci(n):
	current = 0
	after = 1
	for i in range(0,n):
		# this is valid because in multiple assigments first the
		# expressions are evaluated and then they are assigned		
		current, after = after, current + after
	# return the fibonacci number
	return current

# test code
print fibonacci(36)