# P_Lexer Class
from sly import Lexer

class P_Lexer(Lexer):
    tokens = {VARIABLE, NUMBER, STRING, WRITE, READ, IF, THEN, ELSIF, 
        ELSE, WHILE, DEF, COMPARISON, DATA_TYPES, LOGICAL_OPERATORS, 
        SKIP, STOP, RETURN, SH_OPERATORS, TRUE, FALSE}
    
    # Ignored character
    # ignore = '\t '

    # Define tokens
    SH_OPERATORS = r'\+=|-=|\*=|/=|%='
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '%', ':', '&', ' ', '\t'}
    DATA_TYPES = r'INT|FLOAT|DOUBLE|STRING|BOOLEAN'
    TRUE = r'TRUE'
    FALSE = r'FALSE'
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
    LOGICAL_OPERATORS = r'AND|OR|NOT'

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

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
