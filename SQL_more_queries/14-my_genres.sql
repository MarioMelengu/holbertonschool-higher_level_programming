-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tv_genres.name AS name FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
		LEFT JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		WHERE tv_shows.title = 'Dexter'
		GROUP BY name
		ORDER BY name;