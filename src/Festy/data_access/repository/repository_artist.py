from Festy.metier.model.models import Artist

class RepositoryArtist:

    def add_artist(self, artist:Artist):
       artist.save()
       return artist

    def get_artist_by_id(self, artist_id):
        return Artist.objects.get(id=artist_id)

    def get_all_artists(self):
        return Artist.objects.all()

    def update_artist(self,artist:Artist):
        artist.save()
        return artist
        
    def delete_artist(self, artist:Artist):
        artist.delete()
        return artist

       




