-- list shows
SELECT show.title, genre.genre_id
FROM tv_shows AS show
INNER JOIN tv_show_genres AS genre
ON show.id = genre.id
ORDER BY show.title, genre.genre_id;
