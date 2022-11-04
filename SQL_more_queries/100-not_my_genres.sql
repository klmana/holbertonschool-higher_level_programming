-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
  (SELECT tv_genres.name
   FROM tv_genres
   LEFT JOIN tv_show_genres
   ON tv_show_genres.genre_id = tv_genres.id
   RIGHT JOIN tv_shows
   ON tv_shows.id=tv_show_genres.show_id
   AND tv_show_title = 'Dexter')
ORDER BY tv_genres.name ASC;
