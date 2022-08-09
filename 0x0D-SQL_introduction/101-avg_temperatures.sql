-- Select by group --
SELECT city, AVG(value) FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
