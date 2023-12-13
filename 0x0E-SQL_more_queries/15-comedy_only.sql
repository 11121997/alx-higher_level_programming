-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id=id
JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY title;
