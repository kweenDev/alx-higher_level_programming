-- List all cities along with their corresponding states from the hbtn_0d_usa database using only SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
