# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

def hash_string(keyword,buckets):
	tSum = 0
	for ch in keyword:
		tSum += ord(ch)
	return tSum % buckets

print hash_string('a',12)
print hash_string('udacity',12)