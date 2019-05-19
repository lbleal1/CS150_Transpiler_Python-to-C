# P_Parser class
from sly import Parser
from P_Lexer import P_Lexer

class P_Parser(Parser):
    tokens = P_Lexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '%', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }

    # ERROR: previosly defined (LINE 98)
    # @_('')
    # def statement(self, p):
    #     pass

    @_('WRITE "(" STRING ")"')
    def statement(self, p):
        return ('write_stmt', p.STRING)

    @_('READ "(" STRING "," VARIABLE ")"')
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