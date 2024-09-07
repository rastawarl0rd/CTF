#!/bin/env python3
import sys

#Grab file and get uppercase letters

def filter_uppercase(filename):
	with open(filename, 'r') as file:
		content = file.read()
		filtered_content = ''.join( ch for ch in content if ch.isupper())
	return filtered_content

filename = sys.argv[1]

result = filter_uppercase(filename)

print('\n' +  '\t' + result)
