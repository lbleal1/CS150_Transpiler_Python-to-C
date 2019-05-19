from sly import Lexer
import sys

class P_Lexer(Lexer):
    tokens = { VARIABLE, NUMBER, STRING, WRITE, READ, IF, THEN, ELSIF, ELSE, FOR, WHILE, DEF, COMPARISON, OPERANDS, DATA_TYPES, LOGICAL_OPERATORS, SKIP, STOP, RETURN, BLOCKS, IN, RANGE, SH_OPERATORS }
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



if __name__ == '__main__':
    lexer = P_Lexer()
    env = {}
    
    P_File = open(sys.argv[1], "r")
    P_Lines = P_File.readlines()
    P_File.close()

    for index, current_line in enumerate(P_Lines):
        current_line = current_line.rstrip()
        lex = lexer.tokenize(current_line)
        for token in lex:
            print(token.type+"\t===>\t"+str(token.value))
