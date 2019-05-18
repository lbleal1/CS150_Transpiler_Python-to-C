import globals

def pirate_translator(arr_tokens,prime_str):
	#debug()
	global prime_stack
	global prime_flag
	global prime_main
	current_token = []
	#[0]=read ; [1]=print; [2]=loop; [3]=semicolon
	flag_set = [0,0,0,0]
	init = "i"
	pow_flag,pow_flag2 = 0,0

	for i, tokens in enumerate(arr_tokens[0]):
		tok_len = len(current_token)
		#####tab?#####

		#####variables#####
		if(tokens == globals.idty and flag_set[0] == 0	and flag_set[2] == 0 and pow_flag == 0):
			arr_tokens[1][i] = arr_tokens[1][i].replace(' ','')
			prime_str += arr_tokens[1][i].replace('var_','')
		if((tokens == globals.integer or tokens == globals.floating) and pow_flag == 0):
			prime_str += arr_tokens[1][i]
		
		#####built in pow function#####
		#if y var
		if(tokens == globals.idty and pow_flag2 == 1):
			arr_tokens[1][i] = arr_tokens[1][i].replace(' ','')
			prime_str += arr_tokens[1][i].replace('var_','')
			prime_str += ")"
			pow_flag2 = 0
			pow_flag = 0
		#if x var
		if(tokens == globals.idty and pow_flag == 1 and pow_flag2 == 0):
			arr_tokens[1][i] = arr_tokens[1][i].replace(' ','')
			prime_str += arr_tokens[1][i].replace('var_','')
			prime_str += ","
			pow_flag2 = 1
		#if y int
		if((tokens == globals.integer or tokens == globals.floating) and pow_flag2 == 1):
			prime_str += arr_tokens[1][i]
			prime_str += ")"
			pow_flag2 = 0
			pow_flag = 0
		#if x int
		if((tokens == globals.integer or tokens == globals.floating) and pow_flag == 1 and pow_flag2 == 0):
			prime_str += arr_tokens[1][i]
			prime_str += ","
			pow_flag2 = 1

		#####operations#####
		if(tokens == globals.oper):
			arr_tokens[1][i] = arr_tokens[1][i].strip()
			#modulo
			if(arr_tokens[1][i] == '%'):
				prime_str += "%"
				current_token.append("%")
			#addition
			if(arr_tokens[1][i] == '+'):
				prime_str += "+"
				current_token.append("+")
			#subtraction
			if(arr_tokens[1][i] == '-'):
				prime_str += "-"
				current_token.append("-")
			#multiplication
			if(arr_tokens[1][i] == '*'):
				prime_str += "*"
				current_token.append("*")
			#special : exponent
			if(arr_tokens[1][i] == '#'):
				prime_str += "pow("
				pow_flag = 1
				current_token.append("pow")
			#division
			if(arr_tokens[1][i] == '/'):
				prime_str += "/"
				current_token.append("/")

		#####comparators#####
		#equals
		if(tokens == globals.equate):
			prime_str += " = "
			current_token.append("=")
		if(tokens == globals.comp):
			#greater than or equal
			if(arr_tokens[1][i]== '>= '):
				prime_str += ">="
				current_token.append(">=")
			#less than or equal
			if(arr_tokens[1][i] == '<= '):
				prime_str += "<="
				current_token.append("<=")
			#equal
			if(arr_tokens[1][i] == '== '):
				prime_str += "=="
				current_token.append("==")
			#greater than
			if(arr_tokens[1][i] == '> '):
				prime_str += ">"
				current_token.append("> ")
			#less than
			if(arr_tokens[1][i] == '< '):
				prime_str += "<"
				current_token.append("< ")
		#not symbol
		if(tokens == globals.nots):
			prime_str += "!"
			current_token.append("!")	

		#####logic gates#####
		if(tokens == globals.logic_gates):
			if(arr_tokens[1][i])== '&& ':
				prime_str += "&& "
				current_token.append("&&")
			#less than or equal
			if(arr_tokens[1][i]) == '|| ':
				prime_str += "|| "
				current_token.append("||")

		#####boolean#####
		if(tokens == globals.boolean):
			if(arr_tokens[1][i] == "aye"):
				prime_str += "true"
				current_token.append("true")
			if(arr_tokens[1][i] == "nay"):
				prime_str += "false"
				current_token.append("false")
		
		####data types#####
		#read globals.fathom to int
		if(tokens == globals.fathom and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "int "
			current_token.append("int")
		#read league to float
		if(tokens == globals.league and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "float "
			current_token.append("float ")
		#read draft to char
		if(tokens == globals.draft and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "char "
			current_token.append("char")
		#read cutlass to double
		if(tokens == globals.cutlass and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "double "
			current_token.append("double")
		#read argh_globals.fathom to int[]
		if(tokens == globals.argh_fathom and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "int "
			current_token.append("int_arr")
		#read argh_league to float[]
		if(tokens == globals.argh_league and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "float "
			current_token.append("float_arr")
		#read argh_draft to char[]
		if(tokens == globals.argh_draft and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "char "
			current_token.append("char_arr")
		#read argh_cutlass to double[]
		if(tokens == globals.argh_cutlass and flag_set[0] == 0 and flag_set[1] == 0):
			prime_str += "double "
			current_token.append("double_arr")
		#open [ of array
		if(tokens == globals.idty and tok_len == 1 and (current_token[0] == "int_arr" or current_token[0] == "float_arr"
			or current_token[0] == "char_arr" or current_token[0] == "double_arr")):
			prime_str += "["
			current_token.append("[")
		#case 1 of close ] of array
		if(tok_len == 2 and (current_token[0] == "int_arr" or current_token[0] == "float_arr"
			or current_token[0] == "char_arr" or current_token[0] == "double_arr") and current_token[1] == "["):
			prime_str += "]"
			current_token.append("]")
		if(tokens == globals.sq_op and arr_tokens[0][i-1] == globals.idty):
			prime_str += "["
		if(tokens == globals.sq_cl and (arr_tokens[0][i-1] == globals.idty or arr_tokens[0][i-1] == globals.integer)):
			prime_str += "]"

		#####printf function######
		if(tokens == globals.parley):
			prime_str += "printf("
			current_token.append("printf")
			flag_set[1] = 1
		#print int
		if(tokens == globals.fathom and flag_set[0] == 0 and flag_set[1] == 1):
			prime_str += '"%d",'
			current_token.append("int")
		#print float
		if(tokens == globals.league and flag_set[0] == 0 and flag_set[1] == 1):
			prime_str += '"%f",'
			current_token.append("float")
		#print char
		if(tokens == globals.draft and flag_set[0] == 0 and flag_set[1] == 1):
			prime_str += '"%c",'
			current_token.append("char")
		#print string
		if(tokens == globals.argh_draft and flag_set[0] == 0 and flag_set[1] == 1):
			prime_str += '"%s",'
			current_token.append("string")	
		#print double
		if(tokens == globals.cutlass and flag_set[0] == 0 and flag_set[1] == 1):
			prime_str += '"%lf",'
			current_token.append("double")
		#case 1 for ending printf
		if(tokens == globals.string and "printf" in current_token):
			prime_str += arr_tokens[1][i]
			prime_str += ")"
			current_token.append(")")
			flag_set[1] = 0
		#case 2 for ending printf
		if(tokens == globals.idty and "printf" in current_token):
			# debug()
			prime_str += ")"
			current_token.append(")")
			flag_set[1] = 0

		#####scanf function#####
		if(tokens == globals.plunder):
			prime_str += "scanf("
			current_token.append("scanf(")
			flag_set[0] = 1
		#scan variable
		if(tokens == globals.idty and flag_set[0] == 1):
			prime_str += arr_tokens[1][i].replace('var_','')
			prime_str += ")"
			current_token.append(")")
			flag_set[0] = 0
		#scan int
		if(tokens == globals.fathom and arr_tokens[0][i-1] == globals.plunder):
			prime_str += '"%d",&'
		#scan flot
		if(tokens == globals.league and arr_tokens[0][i-1] == globals.plunder):
			prime_str += '"%f",&'
			current_token.append('%f')
		#scan character
		if(tokens == globals.draft and arr_tokens[0][i-1] == globals.plunder):
			prime_str += '"%c",'
			current_token.append('%c')
		#scan string
		if(tokens == globals.argh_draft and arr_tokens[0][i-1] == globals.plunder):
			prime_str += '"%s",'
			current_token.append('%s')
		#scan double
		if(tokens == globals.cutlass and arr_tokens[0][i-1] == globals.plunder):
			prime_str += '"%lf",&'
			current_token.append('%lf')
		#scan char or string pointer
		if(tokens == globals.ptr and (arr_tokens[0][i-1] == globals.draft or arr_tokens[0][i-1] == globals.argh_draft)):
			prime_str += '&'
			current_token.append('ptr')

		#####conditionals#####
		#if
		if(tokens == globals.galley):
			prime_str += "if"
			current_token.append("if")
		#else if
		if(tokens == globals.heave_ho):
			prime_str += "else if"
			current_token.append("else if")
		#else
		if(tokens == globals.heave):
			prime_str += "else"
			current_token.append("else")

		#####loop#####
		#for loop 1
		if(tokens == globals.walk):
			prime_str += "for("	
			current_token.append("for(")
			flag_set[2] = 1
		#for loop 2
		if(tokens == globals.open_par and arr_tokens[0][i-1] == globals.walk):	
			 continue
		if(tokens == globals.the_plank):
			prime_str += ";"
			current_token.append("the_plank")
		if(tokens == globals.idty and arr_tokens[0][i-2] == globals.walk and flag_set[2] == 1):
			init = arr_tokens[1][i].replace('var_','') 				
		if(tokens == globals.idty and flag_set[2] == 1 and arr_tokens[0][i-1] != globals.the_plank):
			prime_str += arr_tokens[1][i].replace('var_','')	
		#for loop 3
		if(tokens == globals.idty and arr_tokens[0][i-1] == globals.the_plank):
			prime_str += init
			prime_str += "<"
			prime_str += arr_tokens[1][i].replace('var_','')
			prime_str += ";"
			prime_str += init
			prime_str += "++)"
		#while loop
		if(tokens == globals.avast):
			prime_str += "while"
			current_token.append("while")


		#####functions#####
		#start bracket
		if(tokens == globals.curly_open and arr_tokens[0][i+1] != globals.open_par):
			prime_str += "{"
			current_token.append("{")
		#end bracket
		if(tokens == globals.curly_close):
			prime_str += "}"
			current_token.append("}")
		#return function
		if(tokens == globals.shiver_me):
			prime_str += "return "
			current_token.append("return")
		#void function
		if(tokens == globals.gangplank):
			prime_str += "void "	
			flag_set[3] = 1
			prime_flag = 1
			current_token.append("void")
		#int function
		if(tokens == globals.parrot):
			prime_str += "int "	
			flag_set[3] = 1
			prime_flag = 1
			current_token.append("int_main")
		#end token function
		if(tokens == globals.scurvy):
			prime_flag = 0
		#parameter set 1
		if(tokens == globals.param1):
			arr_tokens[1][i] = arr_tokens[1][i].replace('fathom', 'int')
			arr_tokens[1][i] = arr_tokens[1][i].replace('league', 'float')
			arr_tokens[1][i] = arr_tokens[1][i].replace('draft', 'char')
			arr_tokens[1][i] = arr_tokens[1][i].replace('var_','')
			prime_str += arr_tokens[1][i]
			current_token.append('gawain')
		#parameter set 2
		if(tokens == globals.param2):
			arr_tokens[1][i] = arr_tokens[1][i].replace('var_','')
			prime_str += arr_tokens[1][i]
			current_token.append(arr_tokens[1][i])
		if('sail_ho' in current_token):
			main_stack = 1

		#####strlen#####
		if(tokens == globals.nautical_len):
			prime_str += "strlen("
			current_token.append("strlen")
		if(tokens == globals.idty and "strlen" in current_token):
			prime_str += ")"

		#####bracketing#####
		if(tokens == 0 and flag_set[2] == 0 and (tok_len > 1 or (tok_len == 1 and not ("{" in current_token or "}" in current_token)))
			and 'sail_ho' not in current_token and "if" not in current_token and "else if" not in current_token and "else" not in current_token 
			and "while" not in current_token and "for" not in current_token and "void" not in current_token and "int_main" not in current_token):
			prime_str += ";"
			current_token = []
		#(
		if(tokens == globals.open_par and flag_set[2] == 0):
			prime_str += "("
			current_token.append("(")
		#)
		if(tokens == globals.close_par and flag_set[2] == 0):
			prime_str += ")"
			current_token.append(")")

	print(prime_str)
	return prime_str

