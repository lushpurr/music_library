import pdb
from models.artists import Artist


artist1 = Artist("Blondie")
artist_repository.save(artist1)
artist2 = Artist("Captain Beefheart")
artist_repository.save(artist2)

album1 = Album("Parallel Lines", "New Wave")
album2 = Album("Glad Music", "Rock")



pdb.set_trace()