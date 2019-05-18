#Wikang Panuos [Translator to C]
#Group Members: Cai, Maravillo, Terrobias, Villamera

import sys 	#for sys.argv
import re	#for regex
import globals 
import tokens_rules
import lexeranalyzer
import syntaxanalyzer #not used -lois
import translator
import parser

def addtab(string, tabcount):
	for i in range(tabcount):
		string += '\t'
	return string


globals.initialize()  
#python name_of_this_program.py program_in_OPL.something
#OPL_file = open(sys.argv[1], "r")
OPL_file = open("sample2.txt", "r")
OPL_lines = OPL_file.readlines()#read all lines and save it
OPL_file.close()				#close it, all is saved in OPL_lines

replace = True
final_string 	= ""
problem_string	= ""
final_string += "#include <stdio.h>\n"
final_string += "#define bool int\n#define true 1\n#define false 0\n\n"
#############################################################
#parsing here
#we append to final_string and problem_string here
	#we also make replace to False if problem_string >= 1
	#check each line separately
globals.main_stack
globals.simula_wakas
globals.mainr

for index, line in enumerate(OPL_lines):			#we need index too, for things like "Line X: something"
	#print index
	line = line.rstrip()							#remove trailing whitespaces
	if (len(line) > 0):
		if globals.main_stack == 0 and globals.mainr == 0:		#isang beses lng
			final_string += "int main(){\n\n"
			globals.mainr = 1
			
		replace, final_string, problem_string = parser.parser(index, line, final_string, problem_string)
		
	final_string += '\n'							#add newline
	"""
	#final_string = addtab(final_string, tabcount)
	#print line
	
	"""
#############################################################

final_string += "\n\treturn 0;\n"
final_string += "}"	
#we only make .exe files when compiling is successful right?
#print final_string
#print replace
if replace == True:
	C_file = open("C_file.c", "w+")
	C_file.write(final_string)
#print problem_string if there's problems
elif replace == False:
	print problem_string
		
