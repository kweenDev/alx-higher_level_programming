-- Display max temperature of each state ordered by state name
SELECT state, MAX(temperature_fahrenheit) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
