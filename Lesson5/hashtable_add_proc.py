# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

# that adds the key to the hashtable (in 
# the correct bucket), with the correct 
# value and returns the new hashtable.

# add an element to the specified bucket
# without looking if it already exist 
def hashtable_add(htable,key,value):
    # find the correct bucket
    bucket = hash_string(key,len(htable))
    htable[bucket].append([key,value])


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


# Code for testing
table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table