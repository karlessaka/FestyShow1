from Festy.metier.model.models import Concert   

class RepositoryConcert:

    def add_concert(self, title, date_time, location, artist, seats_available=150):
        concert = Concert.objects.create(title=title, date_time=date_time, location=location, artist=artist, seats_available=seats_available)
        return concert

    def get_concert_by_id(self, concert_id):
        return Concert.objects.get(id=concert_id)

    def get_all_concerts(self):
        return Concert.objects.all()

    def update_concert(self, title, date_time, location, artist, seats_available, concert_id):
        concert = Concert.objects.get(id=concert_id)
        concert.title = title
        concert.date_time = date_time
        concert.location = location
        concert.artist = artist
        concert.seats_available = seats_available
        concert.save()
        return concert

    def delete_concert(self, concert_id):
        concert = Concert.objects.get(id=concert_id)
        concert.delete()