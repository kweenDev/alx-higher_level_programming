# 0x0E.SQL - More queries
### SQL and MySQL Continuation Project

This project focuses on SQL queries, database management, and understanding MySQL concepts. Below is a summary of the tasks completed in this project along with brief explanations of the terms and learning objectives.

---

#### Learning Objectives:

- **Creating MySQL Users and Managing Privileges:** Understanding how to create new MySQL users, grant privileges to users for databases or tables, and manage user permissions.

- **Primary Key and Foreign Key:** Knowing what a primary key and foreign key are in a database schema, and how they are used to establish relationships between tables.

- **Constraints:** Understanding different constraints such as NOT NULL and UNIQUE constraints and how they enforce data integrity in tables.

- **Data Retrieval:** Learning techniques to retrieve data from multiple tables using JOINs, subqueries, and UNION.

---

#### Tasks Summary:

0. **My Privileges:** Writing a script to list all privileges of specific MySQL users on the server.
   - File: [0-privileges.sql](./0-privileges.sql)
1. **Root User:** Creating a MySQL server user with all privileges.
   - File: [1-create_user.sql](./1-create_user.sql)
2. **Read User:** Creating a database and a user with SELECT privilege only.
   - File: [2-create_read_user.sql](./2-create_read_user.sql)
3. **Always a Name:** Creating a table with a NOT NULL constraint for the name column.
   - File: [3-force_name.sql](./3-force_name.sql)
4. **ID Can't Be Null:** Creating a table with a default value for the ID column and a NOT NULL constraint for the name column.
   - File: [4-never_empty.sql](./4-never_empty.sql)
5. **Unique ID:** Creating a table with a unique constraint on the ID column.
   - File: [5-unique_id.sql](./5-unique_id.sql)
6. **States Table:** Creating a database and a table for states.
   - File: [6-states.sql](./6-states.sql)
7. **Cities Table:** Creating a database and a table for cities with a foreign key constraint.
   - File: [7-cities.sql](./7-cities.sql)
8. **Cities of California:** Listing cities in California without using JOIN.
   - File: [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql)
9. **Cities by States:** Listing cities with their corresponding states using JOIN.
    - File: [9-cities_by_state_join.sql](./9-cities_by_state_join.sql)
10. **Genre ID by Show:** Listing shows with their genre IDs.
    - File: [10-genre_id_by_show.sql](./10-genre_id_by_show.sql)
11. **Genre ID for All Shows:** Listing all shows with their genre IDs or NULL if no genre is linked.
    - File: [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql)
12. **No Genre:** Listing shows without a linked genre.
    - File: [12-no_genre.sql](./12-no_genre.sql)
13. **Number of Shows by Genre:** Counting shows linked to each genre.
    - File: [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql)
14. **My genres:** Listing genres of a specific show.
    - File: [14-my_genres.sql](./14-my_genres.sql)
15. **Only Comedy:** Listing Comedy shows.
    - File: [15-comedy_only.sql](./15-comedy_only.sql)
16. **List shows and genres:** Listing shows with their linked genres.
    - File: [16-shows_by_genre.sql](./16-shows_by_genre.sql)
17. **Not my genre:** Listing shows not linked to the show `Dexter`.
    - File: [100-not_my_genres.sql](./100-not_my_genres.sql)
18. **No Comedy tonight!:** Listing shows without the genre Comedy.
    - File: [101-not_a_comedy.sql](./101-not_a_comedy.sql)
19. **Rotten tomatoes:** Listing shows from hbtn_0d_tvshows_rate by their rating.
    - File: [102-rating_shows.sql](./102-rating_shows.sql)
20. **Best genre:** Listing genres from hbtn_0d_tvshows_rate by their rating.
    - File: [103-rating_genres.sql](./103-rating_genres.sql)

---

### How to Use:
1. Ensure you have MySQL installed (version 8.0.25) and a compatible editor (vi, vim, emacs).
2. Clone the repository: `git clone https://github.com/username/alx-higher_level_programming.git`
3. Navigate to the project directory: `cd alx-higher_level_programming/0x0E-SQL_more_queries`
4. Execute the SQL files using MySQL on your Ubuntu 20.04 LTS system.

---

### Additional Resources:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [MySQL Constraints](https://www.mysqltutorial.org/mysql-constraint/)
- [SQL Technique: Subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
- [SQL Technique: Join Types](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/)
- [MySQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

---

This project provides a comprehensive understanding of MySQL concepts and queries, essential for managing databases effectively in software engineering projects.

Author:
_kweenDev_
Refiloe Radebe
