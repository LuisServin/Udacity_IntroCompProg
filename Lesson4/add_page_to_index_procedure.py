# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 4

# First define an empty list
index = []

# Reusing a existing procedure
def add_to_index(index,keyword,url):
	# check if the keyword already exist
	for entry in index:
		# if first word match
		if entry[0] == keyword:
			# append the url at the end
			entry[1].append(url)
			# exit
			return
	# if it doesn't exists add a new entry
	index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	# Get every word in the page content
	words = content.split()
	for eWord in words:
		add_to_index(index,eWord,url)

add_page_to_index(index,'fake.text',"This is a test")
print index