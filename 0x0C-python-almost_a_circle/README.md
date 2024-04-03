# 0x0C. Python - Almost a circle
#### Python Review Project

## Overview
The Python Review Project is a comprehensive study of Python programming language concepts and features. It covers topics such as unit testing, serialization, deserialization, JSON handling, `*args` and `**kwargs` usage, and more.

## Python Concepts Covered
- Import statements
- Exception handling
- Class definition and usage
- Private attributes
- Getter/Setter methods
- Class methods and static methods
- Inheritance and polymorphism
- Unit testing with unittest framework
- File I/O operations (Read/Write files)
- Usage of `*args` and `**kwargs`
- Serialization and deserialization techniques
- JSON handling

## General Knowledge
In addition to the core Python concepts, you will also gain knowledge in the following areas:
- Understanding and implementing unit testing in large projects
- Serialization and deserialization of Python objects
- Reading and writing JSON files
- Usage of `*args` and `**kwargs` for variable-length argument passing
- Handling named arguments in functions

## Requirements
- Python Scripts
  - Editors: vi, vim, emacs
  - Execution environment: Ubuntu 20.04 LTS with Python 3.8.5
  - Coding standards: PEP 8 compliance (checked with pycodestyle)
  - README.md file: Mandatory at the root of the project folder
  - Executable files with shebang line `#!/usr/bin/python3`
  - Documentation for modules, classes, and functions using `__doc__` strings
- Python Unit Tests
  - Editors: vi, vim, emacs
  - Test files organization: Inside a `tests` folder, following the project's structure
  - Testing framework: unittest module
  - Test file naming convention: `test_*.py`
  - Execution command: `python3 -m unittest discover tests`

## Tasks
The tasks in this project focus on creating Python classes, implementing unit tests, and adhering to PEP 8 standards. Here is a detailed breakdown of the tasks to be completed:

0. **Setting up Project Structure**
   - Create necessary project directories and files.

1. **Base Class Creation**
   - Create a Base class in `models/base.py` for managing the id attribute.

2. **Rectangle Class Creation**
   - Inherit from the Base class to create a Rectangle class in `models/rectangle.py`.

3. **Square Class Creation**
   - Create `Square` class inheriting from `Rectangle`.

4. **Display Instances**
   - Implement a method to display instance information.

5. **Update the Display**
   - Enhance display method with class name and details.

6. **Area Calculation**
   - Implement method to calculate area.

7. **Display Area**
   - Update display to include area information.

8. **Update Area Display**
   - Improve area display for readability.

9. **Update to JSON**
    - Implement JSON serialization and deserialization.

10. **Update JSON Representation**
    - Enhance JSON format for readability.

11. **CSV Serialization**
    - Implement CSV serialization.

12. **CSV Representation**
    - Improve CSV format for readability.

13. **JSON Dictionary Representation**
    - Add method to return dictionary representation.

14. **Dictionary to Instance**
    - Implement method to create instances from dictionary.

15. **File Persistence**
    - Implement file persistence using JSON.

16. **Advanced Instance Creation**
    - Add factory methods for advanced instance creation.

17. **Enhanced File Persistence**
    - Improve file persistence with error handling.

18. **Usage Demonstration**
    - Update README with comprehensive examples.

19. **Final Testing**
    - Conduct final testing and PEP 8 validation.

20. **Documentation**
    - Ensure comprehensive documentation.

21. **Final Review and Submission**
    - Conduct final review and prepare for submission.

## Usage
To run unit tests for the project, execute the following command:
```shell
python3 -m unittest discover tests

*This project has been completed as part of the curriculum for ALX Software Engineering programming by kweenDev.*
