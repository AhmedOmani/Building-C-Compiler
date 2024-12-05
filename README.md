## Building a C Compiler: 

Since my first day in the field of computer science, I have been deeply curious about the inner workings of compilers. How does this incredible piece of technology translate code from one language to another? This curiosity led me to dive into the fascinating world of compiler theory.

To quench my thirst for knowledge, I started reading "Writing a C Compiler" by Nara Sandler. Inspired by the insights from this book, I created this repository to document my journey as I build a simple C compiler from scratch. This project is not just a learning experience but also a way to explore the intricate mechanisms behind this remarkable tool, guided step by step by the book's teachings.

---

## 📜 Project Overview

### 1. **Compiler Driver**
The Compiler Driver orchestrates the compilation process, handling various stages such as:
- **Preprocessing**: Removing comments, expanding macros, and simplifying C source code.
- **Lexical Analysis**: Tokenizing the preprocessed code into meaningful units.
- **Parsing (planned)**: Analyzing token structure to build an Abstract Syntax Tree (AST).
- **Code Generation (planned)**: Emitting assembly or machine code.

The driver supports modular compilation stages with flags for flexibility and debugging.

### 2. **Lexer**
The Lexer (scanner) is responsible for:
- Identifying tokens such as keywords, identifiers, constants, and symbols.
- Ensuring lexical correctness of the source code.
- Reporting and handling errors efficiently.

Tokens are defined using **regular expressions**, making the Lexer both extensible and precise.

### I will add more componentes as i go through the book .
---

## ⚙️ Features

### Compiler Driver
- Modular execution: Choose specific stages using command-line flags (`--lex`, `--parse`, `--codegen`).
- Seamless integration with GCC for preprocessing, assembly, and linking.
- Clear error reporting at each stage of the compilation.

### Lexer
- **Supported Tokens**:
  - `KEYWORD`: C keywords like `int`, `void`, `return`, `printf`.
  - `IDENTIFIER`: User-defined variable and function names.
  - `STRING`: Strings enclosed in quotes.
  - `CONSTANT`: Integer constants.
  - Symbols: Parentheses, braces, commas, and semicolons.
- **Error Handling**: Identifies undefined lexemes with informative messages.
- Efficient tokenization using Python’s **regex library**.

---

## 🔧 Usage

The Compiler Driver accepts a C source file as input and provides flags to control the compilation process.

### Command Syntax
```bash
python compiler_driver.py <source_file.c> [--lex | --parse | --codegen]
```

### Arguments
**<source_file.c>: Path to the C source file**.

**Flags**:
- **--lex**: Perform lexical analysis only.
- **--parse**: Perform lexical analysis and parsing (planned).
- **--codegen**: Perform full compilation up to code generation (planned).


### Full Compilation
```bash
python3 compiler_driver.py test.c
```

### Output:
```plaintxt
Preprocessed test.c to test.i
Compiled test.i to test.s
Executable has been created
```

### Example: Lexical Analysis
```bash
python compiler_driver.py test.c --lex
```

### Output
```plaintxt
Preprocessed test.c to test.i
Lexical analysis is processing..
('KEYWORD', 'int')
('IDENTIFIER', 'main')
...
```
