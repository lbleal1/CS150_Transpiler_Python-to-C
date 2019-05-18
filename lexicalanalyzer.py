import sys
import re 
import globals
import regex_tokens_rules

def lexical_analysis(string,err_idx,error_str):
	arr_tokens = [[],[]]
	list_tokens = regex_tokens_rules.regex_tokens()
	while(string != ''):
		for idx, i in enumerate(list_tokens):
			token_flag = re.match(i[1],string)
			if(token_flag):
				arr_tokens[0].append(i[0])
				arr_tokens[1].append(token_flag.group(0))
				string = string.replace(token_flag.group(0),'')
				if(i[0] < 0):
					error_str += 'Error on Line #' + str(err_idx) + "\n"
					if i[0] == -1:
						error_str += token_flag.group(1) + ' is an invalid variable\n'
					if i[0] == -2:
						error_str += token_flag.group(1) + ' invalid\n'

					return 0,arr_tokens,error_str
				break

	arr_tokens[0].append(0)
	return 1,arr_tokens,error_str