from db.run_sql import run_sql

from models.albums import Album

def save(album):
    sql = "INSERT INTO album (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['artist_id']
    album.artist_id = id
    return album