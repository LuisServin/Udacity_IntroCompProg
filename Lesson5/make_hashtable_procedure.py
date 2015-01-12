# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

# takes as input a number, nbuckets, and returns an empty hash 
# table with n empty buckets

def make_hashtable(nbuckets):
	n = 0
	# initialize an empty list
	table = []
	while n < nbuckets:
		# append an empty element to the list until we have
		# the number of necesary buckets
		table.append([])
		n += 1
	return table