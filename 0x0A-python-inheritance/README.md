# Python OOP Inheritance
### 0x0A-python-inheritance

## Overview
This project consists of a series of Python scripts and test cases designed to explore the concept of inheritance in Python. It covers various aspects, including creating classes, inheritance, method overriding, and class validation.

## Project Structure
The project is organized into several tasks, each addressing specific objectives related to Python inheritance. The tasks are structured as follows:

### Task 0: Lookup
- Implement a function that returns a list of available attributes and methods of an object.

### Task 1: My list
- Create a class `MyList` that inherits from the built-in `list` class, with a method to print the list in ascending order.

### Task 2: Exact same object
- Develop a function `is_same_class` that checks if an object is exactly an instance of a specified class.

### Task 3: Same class or inherit from
- Write a function `is_kind_of_class` to determine if an object is an instance of or inherited from a specified class.

### Task 4: Only sub class of
- Implement a function `inherits_from` that checks if an object is an instance of a class inherited (directly or indirectly) from a specified class.

### Task 5: Geometry module
- Define an empty class `BaseGeometry` to serve as a base class for future extensions.

### Task 6: Improve Geometry
- Extend `BaseGeometry` with a method `area` that raises an exception indicating it is not implemented.

### Task 7: Integer validator
- Create a class `BaseGeometry` with an `integer_validator` method to validate integers.

### Task 8: Rectangle
- Extend `BaseGeometry` to create a `Rectangle` class with width and height attributes, validated by `integer_validator`.

### Task 9: Full rectangle
- Enhance `Rectangle` with an `area` method and a custom string representation using `__str__`.

### Task 10: Square #1
- Create a `Square` class that inherits from `Rectangle` with a constructor for size validation.

### Task 11: Square #2
- Override the string representation of the `Square` class.

### Task 12: My integer
- Develop a class `MyInt` that inherits from `int` with inverted equality and inequality operators.

### Task 13: Can I?
- Implement a function `add_attribute` that adds a new attribute to an object if possible.

## Usage
To run the Python scripts for each task, follow these general steps:

1. Ensure you have Python 3 installed on your system.
2. Open a terminal and navigate to the project directory.
3. Execute the desired script using the `./filename.py` command.
For example, to run Task 0:

```bash
./0-lookup.py
```

## Testing
The project includes test cases for some tasks. To run the tests:

1. Navigate to the `tests` directory.
2. Execute the tests using the command:
```bash
python3 -m doctest ./tests/*
```

### Author
kweenDev

### Acknowledgments
This project is part of the ALX Software Engineering curriculum.
