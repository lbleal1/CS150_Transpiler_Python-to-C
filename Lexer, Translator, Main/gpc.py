from P_Lexer import P_Lexer
from P_Parser import P_Parser
from P_Translator import P_Translator
import sys
import os

def main():
    # Command line format error
    if len(sys.argv) != 3 or not(sys.argv[2].endswith('.p')) or (sys.argv[1] not in ['-t', '-c']):
        print("Invalid arguments.")
        print("Format: python3 gpc.py -flag <name>.p")
        print("Flags:")
        print("-t\tTranslate to C code")
        print("-c\tCompile to .exe file using gcc")
        exit()

    # Filenames
    flag = sys.argv[1]
    filename_p = sys.argv[2]
    filename_c = sys.argv[2].strip('.p') + '.c'

    # Stores code from <name>.p file to P_Lines list
    with open(filename_p, "r") as P_File:
        P_Lines = P_File.readlines()
    
    # Initializes lexer, parser, and translator objects, and result_C string
    lexer = P_Lexer()
    parser = P_Parser()
    translator = P_Translator()
    result_C = "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\n"

    # Translation; line per line
    for index, current_line in enumerate(P_Lines):
        # Lexing, parsing
        current_line = current_line.rstrip()
        tokens = lexer.tokenize(current_line)
        # tree = parser.parse(tokens)
        line_tokens = [token for token in tokens]
        
        # Translation
        if len(line_tokens) != 0:
            result_C += translator.translate_line(line_tokens)
        else:
            result_C += "\n"
        
    # Writes result_C to output file
    with open(filename_c , "+w") as C_File:
        C_File.write(result_C)
        print("Translation done.")
    
    # Compiles if flag is -c
    if flag == '-c':
        os.system("gcc " + filename_c + " -o " + filename_c.strip('.c'))
        print("Compilation done.")


# Calls the main function
if __name__ == '__main__':
    main()