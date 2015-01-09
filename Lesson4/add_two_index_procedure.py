# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 4

index = []

def add_to_index(index,keyword,url):
	# check if the keyword already exist
	for entry in index:
		# if first word match
		if entry[0] == keyword:
			# append the url at the end
			entry[1].append(url)
			# exit
			return
	# if it doesn't exists
	index.append([keyword,[url]])

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index