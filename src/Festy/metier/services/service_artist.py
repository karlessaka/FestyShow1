from Festy.data.repository.repository_artist import RepositoryArtist

class ArtistService:
    def __init__(self):
        self.repository = RepositoryArtist()

    def get_all_artists(self):
        return self.repository.get_all_artists()

    def get_artist_by_id(self, artist_id):
        return self.repository.get_artist_by_id(artist_id)

    def create_artist(self, Full_name, style, email, bio, link):
        return self.repository.add_artist(Full_name, style, email, bio, link)

    def update_artist(self, artist_id, Full_name, style, email, bio, link):
        return self.repository.update_artist(artist_id, Full_name, style, email, bio, link)

    def delete_artist(self, artist_id):
        return self.repository.delete_artist(artist_id)
