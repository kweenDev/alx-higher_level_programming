# 0x02. Python - import & modules

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Tasks

### 0. Import a simple function from a simple file
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition 1 + 2 = 3.

Example:
```bash
$ ./0-add.py
1 + 2 = 3
```

### 1. My first toolbox!
Write a program that imports functions from the file calculator_1.py, performs some calculations, and prints the results.

Example:
```bash
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

### 2. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.

Example:
```bash
$ ./2-args.py
0 arguments.
$ ./2-args.py Hello
1 argument:
1: Hello
$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```

### 3. Infinite addition
Write a program that prints the result of the addition of all arguments.

Example:
```bash
$ ./3-infinite_add.py
0
$ ./3-infinite_add.py 79 10
89
$ ./3-infinite_add.py 79 10 -40 -300 89
-162
```

### 4. Who are you?
Write a program that prints all the names defined by the compiled module hidden_4.pyc.

Example:
```bash
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
```

### 5. Everything can be imported
Write a program that imports the variable a from the file variable_load_5.py and prints its value.

Example:
```bash
$ ./5-variable_load.py
98
```

### 6. Build my own calculator!
Write a program that imports all functions from the file calculator_1.py and handles basic operations.

Example:
```bash
$ ./100-my_calculator.py 3 + 5
3 + 5 = 8
```

### 7. Easy print
Write a program that prints #pythoniscool, followed by a new line, in the standard output.

Example:
```bash
$ ./101-easy_print.py
#pythoniscool
```

### 8. ByteCode -> Python #3
Write the Python function def magic_calculation(a, b): that does exactly the same as the given Python bytecode.

### 9. Fast alphabet
Write a program that prints the alphabet in uppercase, followed by a new line.

Example:
```bash
$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

This project has been completed as part of the ALX Software Engineering program by Refiloe Radebe.
