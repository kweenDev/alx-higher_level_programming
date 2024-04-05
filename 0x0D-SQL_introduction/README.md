# 0x0D.SQL - Introduction

## SQL and MySQL Overview

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. It is used to create, modify, retrieve, and delete data from databases. A database is a structured collection of data organized for efficient retrieval, storage, and management. In the context of this project, hbtn_0c_0 is a database managed using MySQL, an open-source relational database management system (RDBMS). MySQL is widely used for its reliability, scalability, and performance in handling large datasets.

A relational database is a type of database that stores and organizes data into tables with predefined relationships between them. Tables consist of rows and columns, where each row represents a record and each column represents a data attribute. In MySQL, SQL queries are used to interact with relational databases, enabling users to perform operations such as creating tables, inserting, updating, and deleting records, as well as retrieving data based on specific criteria.

The project involves various SQL tasks, including creating and managing databases, tables, and records, performing data analysis, and optimizing database performance. Tasks range from basic operations like listing databases and tables to more advanced tasks like computing averages, filtering data, and handling data conversions. These tasks demonstrate the versatility and power of SQL and MySQL in managing and analyzing data effectively.


## Project Structure

- `README.md`: This readme file providing an overview of the project and its tasks.
- `0-list_databases.sql`: SQL script to list all databases in MySQL server.
- `1-create_database_if_missing.sql`: SQL script to create a database if it doesn't exist.
- `2-remove_database.sql`: SQL script to delete a database if it exists.
- `3-list_tables.sql`: SQL script to list all tables in a specific database.
- `4-first_table.sql`: SQL script to create a table called first_table.
- `5-full_table.sql`: SQL script to display the full description of a table.
- `6-list_values.sql`: SQL script to list all rows of a table.
- `7-insert_value.sql`: SQL script to insert a new row into a table.
- `8-count_89.sql`: SQL script to count records with id = 89 in a table.
- `9-full_creation.sql`: SQL script to create a table and add multiple rows.
- `10-top_score.sql`: SQL script to list records ordered by score.
- `11-best_score.sql`: SQL script to list records with a score >= 10.
- `12-no_cheating.sql`: SQL script to update a record without using id.
- `13-change_class.sql`: SQL script to remove records based on a condition.
- `14-average.sql`: SQL script to compute the average of records in a table.
- `15-groups.sql`: SQL script to list records grouped by a column.
- `16-no_link.sql`: SQL script to list records without a specific value.
- `17-move_to_utf8.sql`: SQL script to convert a database and tables to UTF8.
- `101-avg_temperatures.sql`: SQL script to calculate the average temperature by city.
- `102-top_city.sql`: SQL script to display the top cities' temperatures during specific months.
- `103-max_state.sql`: SQL script to find the maximum temperature of each state.

## Tasks

### Task 0: List databases

Write a script that lists all databases of your MySQL server.

### Task 1: Create a database

Write a script that creates the database hbtn_0c_0 in your MySQL server.

### Task 2: Delete a database

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

### Task 3: List tables

Write a script that lists all the tables of a database in your MySQL server.

### Task 4: First table

Write a script that creates a table called first_table in the current database in your MySQL server.

### Task 5: Full description

Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

### Task 6: List all in table

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

### Task 7: First add

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

### Task 8: Count 89

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

### Task 9: Full creation

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

### Task 10: List by best

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 11: Select the best

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 12: Cheating is bad

Write a script that updates the score of Bob to 10 in the table second_table.

### Task 13: Score too low

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 14: Average

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 15: Number by score

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 16: Say my name

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

### Task 17: Go to UTF8

Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

### Task 18: Temperatures #0

Import in hbtn_0c_0 database this table dump: download

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

### Task 19: Temperatures #1

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

### Task 20: Temperatures #2

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name).

### Author
_kweenDev_
