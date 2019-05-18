import sys
import re 
import globals
import regex_tokens_rules
import lexicalanalyzer
import translator
import parser

def debug():
	print("accessed")


globals.initialize()
prime_stack = 0
prime_main = 0
prime_flag = 0

	#file reading
fname = input("Input file to read: ")
fn = ""
fn += fname[-5:-1]
fn += fname[-1]
if(fn.casefold() == '.abba'):
	file = open(fname, "r")
	line= file.readlines()
	file.close()
	
	#initiate string to `
	prime_str = ""
	prime_str += "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <math.h>\n"
	error_str = ""
		#perform translation and parsing as it traverses string
	for i,lines in enumerate(line):
		lines = lines.rstrip()
		strlen = len(lines)
		if(strlen > 0):	
			validation,prime_str,error_str = parser.pirate_parser(i,lines,prime_str,error_str)

		prime_str += "\n"
		if(prime_flag == 1):
			prime_str += '\t'
			

	#print final string to c file
	#if no error detected -- print
	#else print error
	if(validation == 1):
		write_file = open("pirate_to_c.c", "+w")
		write_file.write(prime_str)

	else:
		print("error with file")
		print(error_str)
else:
	print("\nCan't access file!\n\nCan only access '.abba' files")

