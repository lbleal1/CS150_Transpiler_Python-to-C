from P_Lexer import P_Lexer
from P_Parser import P_Parser
from P_Translator import P_Translator
import sys

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

    # Stores code from <name>.p file to L_Lines list for Lexer
    with open(sys.argv[2], "r") as L_File:
        L_Lines = L_File.readlines()
    
    # Stores code from <name>.p file to P_Lines list for Parser
    with open(sys.argv[2], "r") as P_File:
        Parser_Str = P_File.read()
    
    #print(Parser_Str)

    # Initializes lexer, parser, and translator objects, and result_C string
    lexer = P_Lexer()
    parser = P_Parser()
    translator = P_Translator()
    result_C = "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\n"

    #for tok in lexer.tokenize(Parser_Str):
        #print(tok)
        #print(type(tok.lineno))

    for index, current_line in enumerate(L_Lines):
        # Lexing
        current_line = current_line.rstrip()
        tokens = lexer.tokenize(current_line)
        line_tokens = [token for token in tokens]

        # for token in line_tokens:
            # print(token)
        # Translation
        if len(line_tokens) != 0:
            result_C += translator.translate_line(line_tokens)
        else:
            result_C += "\n"

    # Parsing
    #try:
    #    tree = parser.parse(lexer.tokenize(Parser_Str))
    #except Exception:
    #    tree = "error"
    tree = "yey"

    #print(tree)
        
    # Writes result_C to file PtoC.c
    if tree != "error":
        with open(sys.argv[2].strip('.p').strip('.P') + ".c", "+w") as C_File:
            C_File.write(result_C)
            print("Translation done.")

    if flag == '-c':
        os.system("gcc " + filename_c + " -o " + filename_c.strip('.c'))
        print("Compilation done.")

# Calls the main function
if __name__ == '__main__':
    main()
