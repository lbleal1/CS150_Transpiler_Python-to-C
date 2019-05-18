import globals
def getTokens_and_Rules(tokens_or_rules):	#https://docs.python.org/2/library/re.html <<< check this out

###	local global variables	###
	
	####################################################################################################
	token1 	= [globals.baybayin,	'^(baybayin)(\s+)']	
	token2 	= [globals.bilang,		'^(bilang)(\s+)']					
	token3 	= [globals.lutang,		'^(lutang)(\s+)']				
	token5 	= [globals.talaan_ba,	'^(talaan\[\]baybayin)(\s+)']		
	token6	= [globals.talaan_bi,	'^(talaan\[\]bilang)(\s+)']			
	token7	= [globals.talaan_lu,	'^(talaan\[\]lutang)(\s+)']	
	token8	= [globals.identifier,	'^(_[a-zA-Z][a-zA-Z0-9]*)(\s*)']	
	token9  = [globals.comparison,	'^(>=|<=|==|>|<)(\s*)']				
	token10	= [globals.equals,		'^([=])(\s*)']						
	token11 = [globals.operators,	'^([+]|[-]|[*]|[/]|[%]|butal)(\s*)']
	token12 = [globals.notsymbol,	'^(!)(\s*)']
	token13 = [globals.char,		'^\'.\'(\s*)']
	token14 = [globals.integer,		'^(\d+)(\s*)']
	token15 = [globals.float,		'^(\d+\.\d*)(\s*)']
	token16 = [globals.bool,		'^(tunay|palso)(\s*)']
	token17 = [globals.string,		'^(".+\")(\s*)']
	token18 = [globals.int_arr,		'^\{((\s*)(\d+)(\s*),)*((\s*)(\d+)(\s*))+\}(\s*)']
	token19 = [globals.float_arr,	'^\{((\s*)(\d+|\d+\.\d*)(\s*),)*((\s*)(\d+|\d+\.\d*)(\s*))+\}(\s*)']
	token20 = [globals.and_or,		'^(&&|\|\|)(\s*)']
	
	token23 = [globals.simula,		'^(simula)(\s*)']
	token24 = [globals.gawain,		'^(gawain)(\s+)']
	token25 = [globals.gawin,		'^(gawin)(\s*)']
	token26 = [globals.habang,		'^(habang)(\s+)']
	token27 = [globals.ltpar,		'^(\<)(\s*)']
	token28 = [globals.rtpar,		'^(\>)(\s*)']
	token29 = [globals.hanggang,	'^(hanggang)(\s*)']
	token30 = [globals.wakas,		'^(wakas)(\s*)']
	token31 = [globals.ibalik,		'^(ibalik)(\s*)']
	token32 = [globals.kawalan,		'^(kawalan)(\s*)']
	token33 = [globals.itaga,		'^(itaga)(\s*)']
	token36 = [globals.kada,		'^(kada)(\s*)']
	token37 = [globals.kapag,		'^(kapag)(\s*)']
	token38 = [globals.basahin,		'^(basahin)(\s*)']
	token39 = [globals.katotohanan, '^(katotohanan)(\s+)']
	token40 = [globals.formal_parameters, 
							'^\(((\s*)(globals.baybayin|globals.bilang|globals.lutang|talaan\[\]globals.baybayin|talaan\[\]globals.bilang|talaan\[\]globals.lutang)(\s+)(_[a-zA-Z][a-zA-Z0-9]*)(\s*),)*'+
							'((\s*)(globals.baybayin|globals.bilang|globals.lutang|talaan\[\]globals.baybayin|talaan\[\]globals.bilang|talaan\[\]globals.lutang)(\s+)(_[a-zA-Z][a-zA-Z0-9]*)(\s*))+\)(\s*)']
	token41 = [globals.informal_parameters,
							'^\(((\s*)(_[a-zA-Z][a-zA-Z0-9]*)(\s*),)*'+
							'((\s*)(_[a-zA-Z][a-zA-Z0-9]*)(\s*))+\)(\s*)']
	token21 = [globals.lpar,		'^(\()(\s*)']
	token22 = [globals.rpar,		'^(\))(\s*)']
	#invalid
	invalid1= [-1,			'^_(.*)(\s*)']
	invalid2= [-2,			'^(.+)(\s*)']
	
	tokens = [token1, token2, token3, token5, token6, token7,
			token8, token9, token10, token11, token12,
			token13, token14, token15, token16, token17, token18, token19, token20,
			token40, token41, token23, token24, token25, token26, token27, token28,
			token29, token30, token31, token32, token33, token36, token37, token38,
			token39,token21, token22,
			invalid1, invalid2]
			
	####################################################################################################

	####################################################################################################
	rule1	= [globals.baybayin, globals.identifier]


	rules = [rule1
	]
	####################################################################################################
	if (tokens_or_rules == 0):	return tokens
	if (tokens_or_rules == 1):	return rules
	else:	return [-1]
