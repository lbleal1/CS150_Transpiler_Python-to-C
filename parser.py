import globals
import lexicalanalyzer
import translator

def pirate_parser(idx,string,prime_str,error_str):
	#debug()
	string = string.lstrip('\t')
	flag,arr_tokens, err_tokens = lexicalanalyzer.lexical_analysis(string,idx,error_str)
	if(flag == 0):
		return 0, prime_str,error_str
	prime_str = translator.pirate_translator(arr_tokens,prime_str)
	return 1, prime_str,error_str
