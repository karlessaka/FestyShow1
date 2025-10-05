from Festy.metier.model.models import Artist

class RepositoryArtist:

    def add_artist(self, Full_name, style, email, bio, link):
       artist = Artist.objects.create(Full_name=Full_name, style=style, email=email, bio=bio, link=link)
       return artist

    def get_artist_by_id(self, artist_id):
        return Artist.objects.get(id=artist_id)

    def get_all_artists(self):
        return Artist.objects.all()

    def update_artist(self,  Full_name, style, email,bio, link, artist_id):
        artist = Artist.objects.get(id=artist_id)
        artist.Full_name = Full_name
        artist.email = email
        artist.style = style
        artist.bio = bio
        artist.link = link

    def delete_artist(self, artist_id):
        artist = Artist.objects.get(id=artist_id)
        artist.delete()

       




