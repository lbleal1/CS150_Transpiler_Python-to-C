import globals
import tokens_rules

def syntaxanalysis(tokens, str_index, problem_string):
	
	stack = [1, 8, 0]
	index = 0
	rules = tokens_rules.getTokens_and_Rules(1)
	
	while len(stack) > 0:
		stack_top = stack.pop(0)
		token = tokens[0][index]
		
		if type(stack_top) is int:	#terminal
			if stack_top == token:
				index += 1
				if token == 0:
					if len(stack) == 0:	#ubos na rin stack
						return 1, problem_string
					if len(stack) != 0:	#may natira pa sa rules
						problem_string += 'Line ' + str(str_index+1) + ': '
						problem_string += 'expected a ' + str(stack) + ' sequence afterwards but no more input'
						return 0, problem_string
			else:
				problem_string += 'Line ' + str(str_index+1) + ': '
				problem_string += 'expected a ' + "'%s'" %(dict[stack_top]) + ' but input is: ' + "'%s'"%(dict[token])
				return 0, problem_string
		"""		
		elif type(stack_top) is list:	#nonterminal
			rule = table[svalue][token]
			print('rule', rule)
			for r in reversed(rules[rule]):
				stack.append(r)
				
		print('stack', stack)
		"""
		# temporary list for the tokens for each line