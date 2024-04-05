-- List all the cities of California from the hbtn_0d_usa database without using the JOIN keyword

SELECT id FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
