-- Select ,group by and take average , take top 3 --
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value)
DESC
LIMIT 3;
