import argparse
import os
import subprocess
import sys



def main():
    #Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Compiler Driver")
    parser.add_argument("source_file" , help = "Path to the C source file.")
    parser.add_argument("--lex" , action = "store_true" , help = "Run lexer only.")
    parser.add_argument("--parse" , action = "store_true" , help = "Run lexer and parser.")
    parser.add_argument("--codegen" , action = "store_true" , help = "Run lexer , parser and code generation.")

    args = parser.parse_args()
    source_file = args.source_file

    #Step 1: Preprocess the source file as book mentioned in Chapter1-page7
    preprocessed_file = source_file.replace(".c" , ".i")
    try:
        subprocess.run(["gcc" , "-E" , "-P"  , source_file , "-o" , preprocessed_file])
        print(f"Preprocessed {source_file} to {preprocessed_file}")
    except subprocess.CalledProcessError:
        print("Error during preprocessing")
        sys.exit(1)

    #Step 2 : Compiled preprocessed file to assembly
    assembly_file = source_file.replace(".c" , ".s")
    try:
        subprocess.run(["gcc" , "-S" , preprocessed_file , "-o" , assembly_file])
        print(f"Compiled {preprocessed_file} to {assembly_file}")
    except subprocess.CalledProcessError:
        print("Error during compiling to assembly")
        sys.exit(1)
    finally:
        os.remove(preprocessed_file)

    #Step 3 : assembl & link the assembly file to create executable
    output_file = source_file.replace(".c" , "")
    try:
        subprocess.run(["gcc" , assembly_file , "-o" , output_file])
        print(f"Executable has been created")
        print("Gemed fa45 ya Omani , elcompiler driver finished!")
    except subprocess.CalledProcessError:
        print("Error during assembly and linking!")
        sys.exit(1)
    finally:
        os.remove(assembly_file)


    # Handle --lex flag: Run the lexer and stop
    if args.lex:
        print("Running lexer...")
        # Placeholder for lexer logic
        # You should implement your actual lexer here
        os.remove(preprocessed_file)
        sys.exit(0)
    # Handle --parse flag: Run the lexer and parser, but stop before assembly generation
    if args.parse:
        print("Running lexer and parser...")
        # Placeholder for lexer and parser logic
        # You should implement your actual lexer and parser here
        os.remove(assembly_file)
        sys.exit(0)

    # Handle --codegen flag: Run lexer, parser, and code generation, but stop before code emission
    if args.codegen:
        print("Running full compilation up to code generation...")
        # Placeholder for code generation logic
        # You should implement your lexer, parser, and code generation here
        os.remove(assembly_file)
        sys.exit(0)

if __name__ == "__main__":
    main()
