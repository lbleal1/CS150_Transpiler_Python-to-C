import re	#for regex
import globals
import tokens_rules

def lexanalysis(string, str_index, problem_string):

	tokens = [[],[]]
	tokenlist = tokens_rules.getTokens_and_Rules(0)
	finish = 0
	
	while (string != ''):
		for index, i in enumerate(tokenlist):
			#print i[0]
			valid = re.match(i[1], string)
			#print i[0]
			if valid:
				tokens[0].append(i[0])
				tokens[1].append(valid.group(0))
				#print valid.group(0)
				#print i[0]
				string = string.replace(valid.group(0), '')
				if i[0] < 0:
					problem_string += 'Line ' + str(str_index+1) + ': '
					if i[0] == -1:
						problem_string += '\''+valid.group(1)+'\'' + ' is not a proper variable\n'
					if i[0] == -2:
						problem_string += '\''+valid.group(1)+'\'' + ' no match\n'
					#print problem_string
					return 0, tokens, problem_string
				break
				
	tokens[0].append(0)
	#print tokens[0]
	return 1, tokens, problem_string
	