# 0x0B Python Input/Output

## Description
This project focuses on input/output operations in Python. It covers various topics such as file handling, reading and writing files, JSON serialization, command-line arguments, and more.

## Project Structure
The project directory contains the following files:
1. 0-read_file.py
2. 1-write_file.py
3. 2-append_write.py
4. 3-to_json_string.py
5. 4-from_json_string.py
6. 5-save_to_json_file.py
7. 6-load_from_json_file.py
8. 7-add_item.py
9. 8-class_to_json.py
10. 9-student.py
11. 10-student.py
12. 11-student.py
13. 12-pascal_triangle.py
14. 100-append_after.py
15. 101-stats.py

## File Description
- **0-read_file.py**: Reads a text file (UTF8) and prints its content to stdout.
- **1-write_file.py**: Writes a string to a text file (UTF8) and returns the number of characters written.
- **2-append_write.py**: Appends a string at the end of a text file (UTF8) and returns the number of characters added.
- **3-to_json_string.py**: Converts an onject to a JSON string representation.
- **4-from_json_string.py**: Converts a JSON string to an object.
- **5-save_to_json_file.py**: Saves an object to a file in JSON format.
- **6-load_from_json_file.py**: Loads an object from a JSON file.
- **7-add_item.py**: Adds all command-line arguments to a list, and saves the list to a JSON file.
- **8-class_to_json.py**: Converts a class object to a JSON representation.
- **9-student.py**: Defines a Student class with JSON serialization methods.
- **10-student.py**: Extends Student class with JSON serialization and deserialization methods.
- **11-student.py**: Extends Student classwith file serialization and deserialization methods.
- **12-pascal_triangle.py**: Generates Pascal's Triangle up to a given number of rows. 
- **100-append_after.py**: Inserts a line of text into a file after each line containing a specific string.
- **101-stats.py**: Computes metrics from log data read from stdin.

## Usage

### Running scripts
To run a script, first change it into an executable:

```
chmod +x script_name.py
```
then use the following format:
```bash
python3 script_name.py
```
Replace script_name.py with the actual Python script you want to execute.

## Testing the Log Parsing Script
To test the log parsing script `101-stats.py`, use the provided generator script `101-generator.py` to generate input data. Then, pipe the output of the generator to the stats script:
```bash
./101-generator.py | ./101-stats.py
```

_This project was completed as pat of the ALX Africa Software Engineering programme, by kweenDev._
