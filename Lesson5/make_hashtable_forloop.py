# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

# takes as input a number, nbuckets, and returns an empty hash 
# table with n empty buckets

def make_hashtable(nbuckets):
	table = []
	# now we use the function range to make the code easier to
	# implement this function is explained in the file
	# Notes_Lesson5.txt
	for unused in range(0,nbuckets):
		# Every time we append an empty element
		table.append([])
	return table

print make_hashtable(4)