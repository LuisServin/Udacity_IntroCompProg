# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 6

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
	if s == '':
		return True
	else:
		if s[0] == s[-1]:
			return is_palindrome(s[1:-1])
		else:
			return False

# test Code
print is_palindrome('')
print is_palindrome('abab')
print is_palindrome('abba')