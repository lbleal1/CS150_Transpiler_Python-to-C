import sys 	#for sys.argv
import re	#for regex
import globals 
import tokens_rules
import lexeranalyzer
import syntaxanalyzer #not used -lois
import translator

def parser(str_index, string, final_string, problem_string):

	tabcount = len(string) - len(string.lstrip('\t'))	#count tabs at front
	string = string.lstrip('\t')

	#lexical analysis
	cont, tokens, problem_string = lexeranalyzer.lexanalysis(string, str_index, problem_string)
	#return 1, final_string, problem_string
	if cont == 0: return False, final_string, problem_string
	#syntax analysis (good: lex)
	#cont, problem_string = syntaxanalysis(tokens, str_index, problem_string)
	#if cont == 0: return False, final_string, problem_string
	#translator (good: lex and syntax)
	final_string = translator.translator(tokens, final_string)
	return True, final_string, problem_string
