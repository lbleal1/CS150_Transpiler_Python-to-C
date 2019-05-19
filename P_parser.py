from sly import Lexer
from sly import Parser
import sys

class P_Lexer(Lexer):
    tokens = { VARIABLE, NUMBER, STRING, WRITE, READ, IF, THEN, ELSIF, ELSE, WHILE, DEF, COMPARISON, OPERANDS, DATA_TYPES, LOGICAL_OPERATORS, SKIP, STOP, RETURN, SH_OPERATORS, IDENTIFIER }
    ignore = '\n\t '

    SH_OPERATORS = r'\+=|-=|\*=|/=|%='
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '%', ':', '{', '}' }

    # Define tokens
    IDENTIFIER = r'%d|%s|%f'
    DATA_TYPES = r'INT|FLOAT|DOUBLE|STRING|BOOLEAN'
    LOGICAL_OPERATORS = r'AND|OR|NOT'
    IF = r'IF'
    THEN = r'THEN'
    ELSIF = r'ELSIF'
    ELSE = r'ELSE'
    DEF = r'DEF'
    WHILE = r'WHILE'
    WRITE = r'WRITE'
    READ = r'READ'
    SKIP = r'SKIP'
    STOP = r'STOP'
    RETURN = r'RETURN'
    VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    COMPARISON = r'==|<=|>=|>|<|!='

    @_(r'\d+\.\d+')
    def FLOAT(selt, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

class P_Parser(Parser):
	tokens = P_Lexer.tokens

	precedence = (
        ('left', '+', '-'),
        ('left', '%', '*', '/'),
        ('right', 'UMINUS'),
        )

	def __init__(self):
		self.env = { }

	@_('')
	def statement(self, p):
		pass

	@_('WRITE "(" STRING ")"')
	def statement(self, p):
		return ('write_stmt', p.STRING)

	@_('READ "(" STRING "," VARIABLE")"')
	def statement(self, p):
		return 

	@_('FOR VARIABLE IN RANGE "(" NUMBER "," NUMBER "," NUMBER ")" "{" statement "}"')
	def statement(self, p):
		return ('for_stmt', p.VARIABLE, ('for_cond', p.NUMBER0, ('for_cond', p.NUMBER1, ('for_cond_stmt', p.NUMBER2, p.statement))))

	@_('WHILE condition "{" statement "}"')
	def statement(self, p):
		return ('while_stmt', p.condition, p.statement)

	@_('IF condition THEN "{" statement "}" elsif ELSE "{" statement "}"')
	def statement(self, p):
		return ('if_stmt', ('first_if_stmt', p.condition, p.statement0), ('branch', p.elsif, p.statement1))

	@_('elsif')
	def statement(self, p):
		return (p.elsif)

	@_('')
	def elsif(self, p):
		pass

	@_('ELSIF "{" statement "}" elsif')
	def elsif(self, p):
		return ('elsif.stmt', p.statement, p.elsif)

	@_('statement ";" statement')
	def statement(self, p):
		return('statements', p.statement0, p.statement1)

	@_('DEF VARIABLE "(" params ")" "{" statement "}"')
	def statement(self, p):
		return ('func_def', ('func_init', p.VARIABLE, p.params), p.statement)

	@_('VARIABLE "(" params ")"')
	def statement(self,p):
		return ('func_call', p.VARIABLE, p.params)

	@_('VARIABLE "=" expr')
	def statement(self, p):
		return ('local_Fvar', p.VARIABLE, p.expr)

	@_('expr COMPARISON expr')
	def condition(self, p):
		return ('condition', p.expr0, p.expr1)

	@_('RETURN NUMBER')
	def statement(self, p):
		return ('return_num', p.NUMBER)

	@_('RETURN VARIABLE')
	def statement(self, p):
		return ('return_var', p.VARIABLE)

	@_('var_assign')
	def statement(self,p):
		return p.var_assign

	@_('DATA_TYPES VARIABLE "=" expr')
	def var_assign(self, p):
		return ('var_assign', ('var_declare', p.DATA_TYPES, p.VARIABLE), p.expr)

	@_('DATA_TYPES VARIABLE "=" STRING')
	def var_assign(self, p):
		return ('var_assign', p.VARIABLE, p.STRING)

	@_('params')
	def statement(self, p):
		return (p.params)

	@_('')
	def statement(self, p):
		return (p.params)

	@_('params "," params')
	def params(self, p):
		return ('actual_params', p.params0, p.params1)

	@_('DATA_TYPES params')
	def params(self, p):
		return ('formal_params', p.DATA_TYPES, p.params)

	@_('VARIABLE')
	def params(self,p):
		return (p.VARIABLE)

	@_('NUMBER')
	def params(self,p):
		return (p.NUMBER)

	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('expr "+" expr')
	def expr(self, p):
		return ('add', p.expr0, p.expr1)

	@_('expr "-" expr')
	def expr(self, p):
		return ('sub', p.expr0, p.expr1)

	@_('expr "*" expr')
	def expr(self, p):
		return ('mul', p.expr0, p.expr1)

	@_('expr "/" expr')
	def expr(self, p):
		return ('div', p.expr0, p.expr1)

	@_('expr "%" expr')
	def expr(self, p):
		return ('mod', p.expr0, p.expr1)

	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		return p.expr

	@_('expr SH_OPERATORS NUMBER')
	def expr(self, p):
		return('sh_op', p.expr, p.NUMBER)

	@_('VARIABLE')
	def expr(self, p):
		return ('var', p.VARIABLE)

	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)

		
def translate_line(line_tokens):
	global result_C
	# variables,number stay as they are
	mapping = { "STRING":"char*",
                "INT": "int",
                "FLOAT": "float",
                "WRITE":"printf",
                "READ": "scanf",
                "IF": "if(",
                "ELSE": "else",
                "FOR": "for",
                "WHILE": "while",
                "DEF": "",
                "RETURN": "return",
                "INT": "int",
                "MAIN": "main",
                "AND": "&&",
                "OR": "||",
                "THEN": ")",
                "STOP": "break",
                "SKIP": "continue",
                "ELSIF": "else if(",
                "WHILE": "while"
                }
    for i in range(len(line_tokens)):
		result_C += str(mapping.get(line_tokens[i].value, line_tokens[i].value)) + " "
	if str(line_tokens[len(line_tokens)-1].value) == '{' or str(line_tokens[len(line_tokens)-1].value) == '}':
		result_C += "\n"
	else:
		result_C += ";\n"

if __name__ == '__main__':
	lexer = P_Lexer()
	parser = P_Parser()
	env = {}

	P_File = open(sys.argv[1], "r")
	P_Lines = P_File.readlines()
	P_File.close()

	libraries =  "#include <stdio.h>\n#include<string.h>\n#include<stdlib.h>\n\n\n"
    result_C += libraries
    for index, current_line in enumerate(P_Lines):
        line_tokens =[]
        current_line = current_line.rstrip()
        lex = lexer.tokenize(current_line)
        #tree = parser.parse(lexer.tokenize(text))
        for token in lex:
            line_tokens.append(token) #for each token considering one line
        if len(line_tokens) !=0:
            translate_line(line_tokens)
        else:
            result_C += "\n"
    
write_file = open("PtoC.c", "+w")
write_file.write(result_C)
