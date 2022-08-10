-- select not a commedy 
SELECT title FROM tv_shows
WHERE title NOT IN
(SELECT s.title FROM tv_shows AS s
LEFT JOIN  tv_show_genres AS tg
ON s.id = tg.show_id
LEFT JOIN tv_genres AS g
ON g.id = tg.genre_id
WHERE g.name = "Comedy")
ORDER BY title;
