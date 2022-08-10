-- multiple inner joins
SELECT g.name FROM
tv_shows AS s INNER JOIN
tv_show_genres AS tg
AS s.id = tg.show_id
INNER JOIN tv_genres AS g
ON g.id = tg.genre_id
WHERE s.title = "Dexter" ORDER BY g.name;
