from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated():
    return data_manager.execute_select(f'''SELECT shows.id, shows.title, shows.year, shows.runtime, ROUND(shows.rating,2) AS rating, shows.trailer, shows.homepage,STRING_AGG(genres.name,', ') AS name 
                                           FROM shows 
                                           JOIN show_genres ON show_genres.show_id = shows.id
                                           JOIN genres ON genres.id = show_genres.genre_id
                                           GROUP BY(shows.id)
                                           ORDER BY rating DESC;''')

def get_shows_count():
    return data_manager.execute_select(f'''SELECT COUNT(*) FROM(SELECT shows.id, shows.title, shows.year, shows.runtime, ROUND(shows.rating,2) AS rating, shows.trailer, shows.homepage,STRING_AGG(genres.name,', ') AS name 
                                           FROM shows 
                                           JOIN show_genres ON show_genres.show_id = shows.id
                                           JOIN genres ON genres.id = show_genres.genre_id
                                           GROUP BY(shows.id)
                                           ORDER BY rating DESC) AS something;''')
