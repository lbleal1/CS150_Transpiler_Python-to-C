import globals

def translator(tokens, final_string):

	globals.main_stack
	globals.simula_wakas
	globals.mainr
	
	tokenInLine = []	
	willRead = False
	willLoop = False
	willPrint = False
	willSemiColon = False
	initial = "i"
	for index, eachtoken in enumerate(tokens[0]):
		if eachtoken == globals.identifier and willRead == False and willLoop == False:
			final_string += tokens[1][index].replace('_','')	
		if eachtoken == globals.integer:
			final_string += tokens[1][index]
		if eachtoken == globals.float:
			final_string += tokens[1][index]
		
		bracketOnly = ("{" in tokenInLine or "}" in tokenInLine)
		if eachtoken == globals.end and willLoop == False and 'gawain' not in tokenInLine and ((len(tokenInLine) > 1) or (len(tokenInLine) == 1 and not bracketOnly)) and "if" not in tokenInLine :
			final_string += ";"
			tokenInLine = []
		if eachtoken == globals.lpar and willLoop == False:
			final_string += "("	
			tokenInLine.append("(")
		if eachtoken == globals.rpar and willLoop == False:
			final_string += ")"	
			tokenInLine.append("(")

# for functions		
		if eachtoken == globals.simula and tokens[0][index+1] != globals.lpar:
			globals.simula_wakas += 1	########################
			final_string += "{ "
			tokenInLine.append("{")
		if eachtoken == globals.wakas:
			globals.simula_wakas -= 1	########################
			if globals.simula_wakas == 0:
				globals.main_stack = 0
				#print "HELLO", globals.simula_wakas
			final_string += " }"
			tokenInLine.append("}")
		if eachtoken == globals.ibalik:
			final_string += "return "
			tokenInLine.append("return")
		if eachtoken == globals.kawalan:
			final_string += "void "	
			tokenInLine.append("void")
		if eachtoken == globals.formal_parameters:
			tokens[1][index] = tokens[1][index].replace('globals.baybayin', 'char')
			tokens[1][index] = tokens[1][index].replace('globals.bilang', 'int')
			tokens[1][index] = tokens[1][index].replace('globals.lutang', 'float')
			tokens[1][index] = tokens[1][index].replace('_','')
			final_string += tokens[1][index]
			tokenInLine.append('gawain')
		if eachtoken == globals.informal_parameters:
			tokens[1][index] = tokens[1][index].replace('_','')
			final_string += tokens[1][index]
			tokenInLine.append(tokens[1][index])
		if 'gawain' in tokenInLine:
			globals.main_stack = 1
			
		
		
		# printing (printf)	
		if eachtoken == globals.itaga:
			final_string += " printf"
			tokenInLine.append("printf")
			willPrint = True
		if eachtoken == globals.string and tokens[0][index-1] == globals.itaga:
			final_string += "("	
			tokenInLine.append("(")
		if eachtoken == globals.identifier and "printf" in tokenInLine:
			final_string += ")"
			willPrint = False
			tokenInLine.append(")")	
		if eachtoken == globals.string and "printf" in tokenInLine:
			final_string += tokens[1][index]
			final_string += ")"
			willPrint = False
			tokenInLine.append(")")
		if eachtoken == globals.baybayin and willRead == False and willPrint == True:
			final_string += '("%c",'
			tokenInLine.append("char")
		if eachtoken == globals.bilang and willRead == False and willPrint == True:
			final_string += '("%d",'
			tokenInLine.append("int")
		if eachtoken == globals.lutang and willRead == False and willPrint == True:
			final_string += '("%f",'
			tokenInLine.append("float")		

		# reading (scanf)	
		if eachtoken == globals.basahin:
			final_string += 'scanf("' 
			tokenInLine.append("scanf(")
			willRead = True
		if eachtoken == globals.identifier and willRead == True:
			final_string += tokens[1][index].replace('_','')
			final_string += ")"
			tokenInLine.append(")")
			willRead = False	
		if eachtoken == globals.bilang and tokens[0][index-1] == globals.basahin:
			final_string += '%d",&'
		if eachtoken == globals.lutang and tokens[0][index-1] == globals.basahin:
			final_string += '%f",&'
			tokenInLine.append('%f')
		if eachtoken ==  globals.char and tokens[0][index-1] == globals.basahin:
			final_string += '%c",&'
			tokenInLine.append('%c')

#	Data Types
		if eachtoken == globals.baybayin and willRead == False and willPrint == False:
			final_string += "char "
			tokenInLine.append("char")
		if eachtoken == globals.bilang and willRead == False and willPrint == False:
			final_string += "int "
			tokenInLine.append("int")
		if eachtoken == globals.lutang and willRead == False and willPrint == False:
			final_string += "float "
			tokenInLine.append("float")
		
#	Operators,etc
		if eachtoken == globals.equals:
			final_string += " = "
			tokenInLine.append("=")
		if eachtoken == globals.comparison:
			if tokens[1][index] == '>= ':
				final_string += ">="
				tokenInLine.append(">=")
			if tokens[1][index] == '<= ':
				final_string += "<="
				tokenInLine.append("<=")
			if tokens[1][index] == '== ':
				final_string += "=="
				tokenInLine.append("==")
			if tokens[1][index] == '> ':
				final_string += ">"
				tokenInLine.append("> ")
			if tokens[1][index] == '< ':
				final_string += "<"
				tokenInLine.append("< ")
		if eachtoken == globals.notsymbol:
			final_string += "!"
			tokenInLine.append("!")					
		
		if eachtoken == globals.operators:
			tokens[1][index] = tokens[1][index].strip()
			if tokens[1][index] == 'butal':
				final_string += " % "
				tokenInLine.append("%")
			if tokens[1][index] == '+':
				final_string += "+"
				tokenInLine.append("+")
			if tokens[1][index] == '-':
				final_string += "-"
				tokenInLine.append("-")
			if tokens[1][index] == '*':
				final_string += "*"
				tokenInLine.append("*")
			if tokens[1][index] == '/':
				final_string += "/"
				tokenInLine.append("/")			

		if eachtoken == bool:
			if tokens[1][index] == 'tunay':
				final_string += " true "
				tokenInLine.append("true")	
			if tokens[1][index] == 'palso':
				final_string += " false "
				tokenInLine.append("false")	

#	loops
		if index < len(tokens[0])-2:
			if tokens[1][index+1] == "(" and tokens[0][index] == globals.simula:
				final_string += "for("	
				tokenInLine.append("for(")
				willLoop = True
		if eachtoken == globals.lpar and tokens[0][index-1] == globals.simula:	
			 continue
		if eachtoken == globals.hanggang:
			final_string += ";"
			tokenInLine.append("hanggang")	 
		# if eachtoken == globals.identifier and willLoop == True and "upto" not in tokenInLine:
		# 	final_string += tokens[1][index].replace('_','')
		# 	tokenInLine.append("upto")
		# if eachtoken == globals.identifier and willLoop == True and "upto" in tokenInLine:
		# 	final_string += "<"
		# 	final_string += tokens[1][index].replace('_','')
		if eachtoken == globals.identifier and tokens[0][index-2] == globals.simula and willLoop == True:
			initial = tokens[1][index].replace('_','') 				
		if eachtoken == globals.identifier and willLoop == True and tokens[0][index-1] != globals.hanggang:
			final_string += tokens[1][index].replace('_','')	
		if eachtoken == globals.identifier and tokens[0][index-1] == globals.hanggang:
			final_string += initial
			final_string += "<"
			final_string += tokens[1][index].replace('_','')
			final_string += ";"
			final_string += initial
			final_string += "+="
			final_string += "1)"
		if eachtoken == globals.kapag:
			final_string += "if"
			tokenInLine.append("if")	
		if eachtoken == globals.gawin:
			final_string += "do "
			tokenInLine.append("do")	
		if eachtoken == globals.habang:
			final_string += "while "
			tokenInLine.append("while")

	return final_string