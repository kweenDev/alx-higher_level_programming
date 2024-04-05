-- Display average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature_fahrenheit) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
