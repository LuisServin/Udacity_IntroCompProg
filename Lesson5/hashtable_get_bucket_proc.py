# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):
	# the arguments for hash_string function are the keyword
	# and the length of the list it returns the index
	# so we return the actual bucket
	return htable[hash_string(keyword,len(htable))]

# Procedure to find the right bucket for the keyword
# using all its letters
def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

# Procedure from las excersise
def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

# print the result bucket
print hashtable_get_bucket(table, "Zoe")