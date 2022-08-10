-- sub query
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities where state_id =
(select id from states where name = "california") ORDER BY cites.id; 
