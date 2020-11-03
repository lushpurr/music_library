import pdb
from models.artists import Artist
from models.albums import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist1 = Artist("Blondie")
artist_repository.save(artist1)
artist2 = Artist("Captain Beefheart")
artist_repository.save(artist2)

album1 = Album("Parallel Lines", "New Wave")
album_repository.save(album1)
album2 = Album("Safe As Milk", "Rock")
album_repository.save(album2)



pdb.set_trace()