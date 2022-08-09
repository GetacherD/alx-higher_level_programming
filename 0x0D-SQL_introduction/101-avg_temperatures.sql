-- Select by group --
USE `hbtn_0c_0`;
source `temperatures.sql`;
SELECT city, AVG(value) FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
