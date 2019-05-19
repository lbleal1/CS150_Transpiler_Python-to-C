import globals

def regex_tokens():
	#debug()
	t1 = [globals.fathom, '^(fathom)(\s+)']
	t2 = [globals.league, '^(league)(\s+)']
	t3 = [globals.draft, '^(draft)(\s+)']
	t4 = [globals.argh_fathom, '^(argh_fathom)(\s+)']
	t5 = [globals.argh_league, '^(argh_league)(\s+)']
	t6 = [globals.argh_draft, '^(argh_draft)(\s+)']
	t7 = [globals.parley, '^(parley)(\s*)']
	t8 = [globals.plunder, '^(plunder)(\s*)']
	t9 = [globals.gangplank, '^(gangplank)(\s*)']
	t10 = [globals.idty, '^((var)_[a-zA-Z][a-zA-Z0-9]*)(\s*)']
	t11 = [globals.comp, '^(>=|<=|==|>|<)(\s*)']
	t12 = [globals.equate, '^([=])(\s*)']
	t13 = [globals.oper, '^([+]|[-]|[*]|[#]|[/]|[%])(\s*)']
	t14 = [globals.nots, '(!)(\s*)']
	t15 = [globals.integer, '(\d+)(\s*)']
	t16 = [globals.floating, '^(\d+\.\d*)(\s*)']
	t17 = [globals.char, '^\'.\'(\s*)']
	t18 = [globals.int_arr, '^\{((\s*)(\d+)(\s*),)*((\s*)(\d+)(\s*))+\}(\s*)']
	t19 = [globals.float_arr, '^\{((\s*)(\d+|\d+\.\d*)(\s*),)*((\s*)(\d+|\d+\.\d*)(\s*))+\}(\s*)']
	t20 = [globals.string, '^(".+\")(\s*)']
	t21 = [globals.sail_ho, '^(sail_ho)(\s+)']
	t22 = [globals.open_par, '^(\()(\s*)']
	t23 = [globals.close_par, '^(\))(\s*)']
	t24 = [globals.galley, '^(galley)(\s*)']
	t25 = [globals.heave_ho, '^(heave_ho)(\s*)']
	t26 = [globals.heave, '^(heave)(\s*)']
	t27 = [globals.boolean, '^(aye|nay)(\s*)']
	t28 = [globals.avast, '^(avast)(\s*)']
	t29 = [globals.rig, '^(rig)(\s*)']
	t30 = [globals.curly_open, '^(\{)(\s*)']
	t31 = [globals.curly_close, '^(\})(\s*)']
	t32 = [globals.shiver_me, '^(shiver_me)(\s*)']
	t33 = [globals.parrot, '^(parrot)(\s*)']
	t34 = [globals.walk, '^(walk)(\s*)']
	t35 = [globals.the_plank, '^(the_plank)(\s*)']
	t36 = [globals.scurvy, '^(scurvy)(\s*)']
	t37 = [globals.nautical_len, '^(nautical_len)(\s*)']
	t38 = [globals.cutlass, '^(cutlass)(\s+)']
	t39 = [globals.ptr, '^(ptr)(\s+)']
	t40 = [globals.argh_cutlass, '^(argh_cutlass)(\s+)']
	t41 = [globals.logic_gates, '^(&&|\|\|)(\s*)']
	t42 = [globals.sq_op, '^(\[)(\s*)']
	t43 = [globals.sq_cl, '^(\])(\s*)']

	t50 = [globals.param1, '^\(((\s*)(fathom|league|draft|cutlass|argh_|argh_league|argh_draft|argh_cutlass)(\s+)((var)_[a-zA-Z][a-zA-Z0-9]*)(\s*),)*'+
	      '((\s*)(fathom|league|draft|cutlass|argh_fathom|argh_league|argh_draft|argh_cutlass(\s+)((var)_[a-zA-Z][a-zA-Z0-9]*)(\s*))+\)(\s*)']
	t51 = [globals.param2, '^\(((\s*)((var)_[a-zA-Z][a-zA-Z0-9]*)(\s*),)*'+
		  '((\s*)((var)_[a-zA-Z][a-zA-Z0-9]*)(\s*))+\)(\s*)']

	re_tokens = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,
				t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,
				t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,
				t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,
				t41,t42,t43,
				t50,t51]
	return re_tokens

def regex_rules():
	rules = [globals.draft,globals.idty]
	rules_set = [rules]
	return rules_set