-- select sum rating of genres
SELECT g.name, SUM(r.rate) AS rating FROM tv_genres AS g
INNER JOIN tv_show_genres AS tg ON g.id = tg.genre_id
INNER JOIN tv_shows AS s
ON s.id = tg.show_id
INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
