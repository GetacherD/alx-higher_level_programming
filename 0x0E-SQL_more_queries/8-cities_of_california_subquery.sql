-- sub query
SELECT cities.id, cities.name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = "california") ORDER BY cites.id; 
