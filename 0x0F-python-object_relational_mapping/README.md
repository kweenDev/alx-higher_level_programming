# 0x0F. Python - Object-relational mapping
# ORM Project with SQLAlchemy and MySQLdb

## Overview

This project demonstrates the use of SQLAlchemy, an Object-Relational Mapper (ORM), with MySQL databases using MySQLdb. It provides examples of connecting to a MySQL database, querying data, and using ORM to abstract database interactions.

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Ubuntu 20.04 LTS

## Setup

1. **Create Python Virtual Environment**:
```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

2. **Install MySQLdb and SQLAlchemy**:
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ sudo pip3 install SQLAlchemy
```

3. **Run the Code**:
- Execute the Python scripts provided in this project.

## File Structure

- `connect_mysql.py`: Demonstrates connecting to a MySQL database using MySQLdb.
- `orm_example.py`: Shows ORM usage with SQLAlchemy for MySQL databases.
- `README.md`: This file, providing project overview and setup instructions.

## Usage

1. **Connect to MySQL Database**:
- Run `connect_mysql.py` to connect and execute SQL queries directly.

2. **Use SQLAlchemy ORM**:
- Run `orm_example.py` to demonstrate ORM mapping and object interactions with the database.

## Resources

- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)

## Contributors

- Refiloe Radebe (_kweenDev_)
- Date of Creation: April 30, 2024

