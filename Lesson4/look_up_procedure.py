# !usr/bin/env python

# Code from 
# Introduction to Computer Programming in Udacity
# Lesson 4

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []

print lookup(index,'udacity')
print lookup(index,'mechanical')