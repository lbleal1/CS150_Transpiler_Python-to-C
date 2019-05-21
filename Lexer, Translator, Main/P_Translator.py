# Translator class
class P_Translator:
    def __init__(self):        
        self.mapping = { 
            "STRING":"char*",
            "INT": "int",
            "FLOAT": "float",
            "DOUBLE": "double",
            "BOOL": "bool",
            "WRITE":"printf",
            "READ": "scanf",
            "IF": "if(",
            "ELSE": "else",
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
            "WHILE": "while(",
            "TRUE": "true", 
            "FALSE": "false"}

    def translate_line(self, line_tokens):
        result = ""
        for token in line_tokens:
            result += str(self.mapping.get(token.value, token.value)) + ""

        if str(line_tokens[-1].value) not in ['{', '}']:
            result += ";"  
        result += "\n"        
        return result
