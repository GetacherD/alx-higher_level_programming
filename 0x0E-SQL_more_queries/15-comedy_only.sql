-- select comedy only
SELECT s.title FROM
tv_genres AS g
INNER JOIN tv_show_genres AS tg
ON g.id = tg.genre_id
INNER JOIN tv_shows AS s
ON s.id = tg.show_id
WHERE g.name = "Comedy"
ORDER BY s.title;
