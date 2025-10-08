from Festy.data_access.repository.repository_concert import RepositoryConcert

class ConcertService:
    def __init__(self):
        self.repository = RepositoryConcert()

    def get_all_concerts(self):
        return self.repository.get_all_concerts()

    def get_concert_by_id(self, concert_id):
        return self.repository.get_concert_by_id(concert_id)

    def create_concert(self, title, date_time, location, artist, seats_available=150):
        return self.repository.add_concert(title, date_time, location, artist, seats_available)

    def update_concert(self, concert_id, title, date_time, location, artist, seats_available):
        return self.repository.update_concert(title, date_time, location, artist, seats_available, concert_id)

    def delete_concert(self, concert_id):
        return self.repository.delete_concert(concert_id)