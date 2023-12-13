-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT name AS genre, COUNT(8) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows desc;
