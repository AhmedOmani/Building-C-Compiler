### This repository for implementing C compiler from scratch 


### Compiler Driver
This repository contains a Compiler Driver (CD) implemented in Python. The CD is a key component for compiling C source files into executable programs, managing the entire compilation process, which includes preprocessing, compiling to assembly, and linking.

## Overview
A Compiler Driver is crucial for managing the sequence of steps needed to transform a high-level C source code file into an executable binary. This implementation leverages GCC to handle preprocessing, assembly generation, and linking.

## Features
- Preprocessing: Uses GCC to preprocess the source file and generate an intermediate file.
- Compilation: Compiles the preprocessed file to assembly.
- Assembly and Linking: Uses GCC to assemble and link the assembly file, creating the final executable.
- Intermediate Stages: Supports options to test intermediate stages (e.g., --lex, --parse, --codegen).
