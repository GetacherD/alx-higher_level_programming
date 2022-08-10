-- list all cities
SELECT cities.id, cities.name, states.name FROM cities, states where states.id = cities.state_id;
