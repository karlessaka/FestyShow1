from Festy.data_access.repository.repository_artist import RepositoryArtist
from Festy.metier.model.models import Artist


class ArtistService:
    def __init__(self):
        self.repository = RepositoryArtist()

    def create_artist(self, data: dict):
        artist = Artist(**data)
        return self.repository.add_artist(artist)

    def update_artist(self, artist_id, data):
        artist = self.repository.get_artist_by_id(artist_id)
        for field, value in data.items():
            setattr(artist, field, value)
        artist.save()
        return artist
    
    def get_all_artists(self):
        return self.repository.get_all_artists()

    def get_artist_by_id(self, artist_id):
        return self.repository.get_artist_by_id(artist_id)


    def delete_artist(self, artist_id):
        artist = self.repository.get_artist_by_id(artist_id)
        return self.repository.delete_artist(artist)
