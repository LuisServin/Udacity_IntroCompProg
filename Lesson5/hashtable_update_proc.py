# !usr/bin/env python

# Code from 
# Introduction to Computer Science in Udacity
# Lesson 5

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# this procedure update the value associated with a keyword if
# it already exists, if not added to the corresponding bucket
def hashtable_update(htable,key,value):
	# find the correct bucket
	bucket = hashtable_get_bucket(htable,key)
	# search in the correct bucket
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value
			return htable
	bucket.append([key,value])
	return htable

# Procedure to lookup in a hashtable, if the element is not
# in the hash table return None
def hashtable_lookup(htable,key):
	# Find the correct bucket
	bucket = hash_string(key,len(htable))
	# search in the bucket for the keyword, if we find it then
	# return the value associated with
	for e in htable[bucket]:
		if e[0] == key:
			return e[1]
	# if not found return None
	return None

def hashtable_add(htable,key,value):
    # find the correct bucket
    bucket = hash_string(key,len(htable))
    # append the new element to that bucket
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

# code to test
table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table