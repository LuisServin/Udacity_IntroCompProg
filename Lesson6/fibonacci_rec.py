# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 6

# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(0)
print fibonacci(1)
print fibonacci(15)