# 0x08. Python - More Classes and Objects

## Overview
This project focuses on enhancing your understanding of Object-Oriented Programming (OOP) concepts in Python. The tasks involve creating a class named Rectangle and implementing various methods and attributes to handle rectangle-related operations.

## Learning Objectives
After completing this project, you should be able to:

- Understand the fundamentals of Python programming.
- Grasp the principles of Object-Oriented Programming (OOP).
- Implement and use classes, objects, and methods in Python.
- Work with attributes, properties, and class methods.
- Explore advanced concepts like static methods, class attributes, and class methods.
- Gain proficiency in string representation, evaluation, and instance deletion in Python.

## Key Concepts
#### 1. Classes and Objects
In Python, everything is an object, and a class acts as a blueprint for creating objects. An object is an instance of a class, representing a concrete entity based on the class's blueprint.

#### 2. Attributes and Methods
Attributes are the characteristics of an object, while methods are functions within a class that perform actions on the object.

#### 3. Initialization with `__init__`
The `__init__` method is a special constructor in Python classes, called when an object is created. It is used for initializing object attributes.

#### 4. Data Abstraction and Encapsulation
OOP in Python promotes data abstraction, hiding implementation details, data encapsulation, binding data and methods, and information hiding, restricting access to certain details.

#### 5. Properties and Attributes
Properties are special attributes with getter, setter, and deleter methods, providing controlled access to object attributes.

#### 6. Special Methods- `__str__` and `__repr__`
These methods define the string representation of an object. `__str__` is for `str()`, and `__repr__` is for `repr()`.

## Project Structure
The project consists of several tasks, each building on the previous one. Here's a brief overview of each task:

0. Simple Rectangle (0-rectangle.py):
- Create an empty class `Rectangle` that defines a rectangle.

1. Real Definition of a Rectangle (1-rectangle.py):
- Add private instance attributes `width` and `height` with proper getters and setters.
- Implement instantiation with optional width and height.

2. Area and Perimeter (2-rectangle.py):
- Extend the class to include methods for calculating the rectangle's area and perimeter.

3. String Representation (3-rectangle.py):
- Enhance the class to provide a string representation using `print()` and `str()` methods.

4. Eval is Magic (4-rectangle.py):
- Implement `repr()` method for recreating a new instance using `eval()`.

5. Detect Instance Deletion (5-rectangle.py):
- Print a farewell message when an instance of `Rectangle` is deleted.

6. How Many Instances (6-rectangle.py):
- Add a class attribute `number_of_instances` to track the number of instances created.

7. Change Representation (7-rectangle.py):
- Introduce a public class attribute `print_symbol` to customize string representation.

8. Compare Rectangles (8-rectangle.py):
- Implement a static method `bigger_or_equal` to compare rectangles based on area.

9. A Square is a Rectangle (9-rectangle.py):
- Add a class method `square` to create a new instance of `Rectangle` as a square.

10. N queens (101-queens.py):
- Solve the N Queens problem using backtracking. This task is an advanced challenge.

### Author
kweendev
