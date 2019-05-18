def initialize():
	global main_stack
	global mainr
	global simula_wakas
	#global
	global end
	#datatype##############
	global baybayin 
	global bilang 	
	global lutang		
	global talaan_ba
	global talaan_bi	
	global talaan_lu	
	#######################

	global identifier 	
	global comparison	
	global equals	
	global operators		
	global notsymbol		

	#values################
	global char		
	global integer			
	global float			
	global bool		
	global string		
	global int_arr		
	global float_arr	
	#######################

	global and_or		
	global lpar		
	global rpar			
	global simula	
	global gawain		
	global gawin			
	global habang		
	global ltpar			
	global rtpar		
	global hanggang	
	global wakas 	
	global ibalik	
	global kawalan		 
	global itaga	
	global kada		
	global kapag		
	global basahin		
	global katotohanan	
	global formal_parameters
	global informal_parameters 

	global dict

	main_stack = -1
	mainr = 0
	simula_wakas = 0


	#global
	end				= 0
	#datatype##############
	baybayin 		= 1
	bilang 			= 2
	lutang			= 3
	talaan_ba		= 5
	talaan_bi		= 6
	talaan_lu		= 7
	#######################

	identifier 		= 8
	comparison		= 9
	equals			= 10
	operators		= 11
	notsymbol		= 12

	#values################
	char			= 13
	integer			= 14
	float			= 15
	bool			= 16
	string			= 17
	int_arr			= 18
	float_arr		= 19
	#######################

	and_or			= 20
	lpar			= 21
	rpar			= 22
	simula			= 23
	gawain			= 24
	gawin			= 25
	habang			= 26
	ltpar			= 27
	rtpar			= 28
	hanggang		= 29
	wakas			= 30
	ibalik			= 31
	kawalan		  	= 32
	itaga			= 33
	kada			= 36
	kapag			= 37
	basahin			= 38
	katotohanan		= 39
	formal_parameters = 40
	informal_parameters = 41

	dict = {1: 'baybayin', 2: 'bilang', 3: 'lutang', 5: 'talaan[]baybayin', 6: 'talaan[]bilang', 7: 'talaan[]lutang',
			8: 'identifier', 9: 'comparison symbol', 10: 'equal symbol', 11: 'operator symbol', 12: 'not symbol', 13: 'char', 
			14: 'integer', 15: 'float', 16: 'bool', 17: 'string', 18: 'int array', 19: 'float array', 20: 'and/or', 21: ')',
			22: '(', 23: 'simula', 24: 'gawain', 25: 'gawin', 26: 'habang', 27: '<', 28: '>', 29: 'hanggang', 30: 'wakas',
			31: 'ibalik', 32: 'kawalan', 33: 'itaga', 36: 'kada', 37: 'kapag', 38: 'basahin', 39: 'katotohanan', 40: 'formal parameter', 
			41: 'informal parameter'}
