from db.run_sql import run_sql

from models.artists import Artist

def save(artist):
    sql = "INSERT INTO artist (name, id) VALUES (%s, %s) RETURNING *"
    values = [artist.name, artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist