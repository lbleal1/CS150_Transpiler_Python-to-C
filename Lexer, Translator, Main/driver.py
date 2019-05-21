from P_Lexer import P_Lexer
from P_Parser import P_Parser
from P_Translator import P_Translator
import sys

def main():
    # Command line format error
    if (len(sys.argv) != 2 or not(sys.argv[1].endswith('.p'))):
        print("Invalid arguments.")
        print("Format: python3 driver.py <name>.p")
        exit()

    # Stores code from <name>.p file to P_Lines list
    with open(sys.argv[1], "r") as P_File:
        P_Lines = P_File.readlines()
    
    # Initializes lexer, parser, and translator objects, and result_C string
    lexer = P_Lexer()
    parser = P_Parser()
    translator = P_Translator()
    result_C = "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\n"

    for index, current_line in enumerate(P_Lines):
        # Lexing, parsing
        current_line = current_line.rstrip()
        tokens = lexer.tokenize(current_line)
        # tree = parser.parse(tokens)
        line_tokens = [token for token in tokens]
        # for token in line_tokens:
            # print(token)
        # Translation
        if len(line_tokens) != 0:
            result_C += translator.translate_line(line_tokens)
        else:
            result_C += "\n"
        
    # Writes result_C to file PtoC.c
    with open(sys.argv[1].strip('.p').strip('.P') + ".c", "+w") as C_File:
        C_File.write(result_C)


# Calls the main function
if __name__ == '__main__':
    main()