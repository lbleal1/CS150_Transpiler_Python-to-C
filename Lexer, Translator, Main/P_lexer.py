# run this with
# python3 P_lexer.py Test.p
# spits out PtoC.c
# contains P_lexer, translator and main

from sly import Lexer
import sys

result_C = ""

class P_Lexer(Lexer):
    tokens = { VARIABLE, NUMBER, STRING, WRITE, READ, 
                IF, THEN, ELSIF, ELSE, FOR, WHILE, DEF, 
                COMPARISON, OPERANDS, DATA_TYPES, LOGICAL_OPERATORS, 
                SKIP, STOP, RETURN, BLOCKS, IN, RANGE, SH_OPERATORS }
    ignore = '\t '

    SH_OPERATORS = r'\+=|-=|\*=|/=|%='
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '%', ':' }

    # Define tokens
    DATA_TYPES = r'INT|FLOAT|DOUBLE|STRING|BOOLEAN'
    IF = r'IF'
    THEN = r'THEN'
    ELSIF = r'ELSIF'
    ELSE = r'ELSE'
    FOR = r'FOR'
    IN = r'IN'
    DEF = r'DEF'
    WHILE = r'WHILE'
    WRITE = r'WRITE'
    READ = r'READ'
    SKIP = r'SKIP'
    STOP = r'STOP'
    RETURN = r'RETURN'
    RANGE = r'RANGE'
    VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    COMPARISON = r'==|<=|>=|>|<|!='
    LOGICAL_OPERATORS = r'AND|OR|NOT'
    BLOCKS = r'{|}'
    ##OPERANDS = r'\+|-|\*|/|%'

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
    #print("token num",len(line_tokens))
    for i in range(len(line_tokens)):
        result_C += str(mapping.get(line_tokens[i].value, line_tokens[i].value)) + " "
    #print("token:" + str(line_tokens[len(line_tokens)-1].value))
    if str(line_tokens[len(line_tokens)-1].value) == '{' or str(line_tokens[len(line_tokens)-1].value) == '}':
        result_C += "\n"
    else:
        result_C += ";\n"
    

if __name__ == '__main__':
    lexer = P_Lexer()
    env = {}
    
    P_File = open(sys.argv[1], "r")
    P_Lines = P_File.readlines()
    P_File.close()
    
    libraries =  "#include <stdio.h>\n#include<string.h>\n#include<stdlib.h>\n\n"
    result_C += libraries
    for index, current_line in enumerate(P_Lines):
        line_tokens =[]
        current_line = current_line.rstrip()
        lex = lexer.tokenize(current_line)
        for token in lex:
            #print(token)
            line_tokens.append(token) #for each token considering one line
        if len(line_tokens) !=0:
            translate_line(line_tokens)
        else:
            result_C += "\n"
    
write_file = open("PtoC.c", "+w")
write_file.write(result_C)
