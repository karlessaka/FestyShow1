from Festy.data.repository.repository_booking import RepositoryBooking

class BookingService:
    def __init__(self):
        self.repository = RepositoryBooking()

    def get_all_bookings(self):
        return self.repository.get_all_booking()

    def get_booking_by_id(self, booking_id):
        return self.repository.get_booking_by_id(booking_id)

    def create_booking(self, concert, user_name, user_email, code_booking):
        return self.repository.add_booking(concert, user_name, user_email, code_booking)

    def update_booking(self, booking_id, concert, user_name, user_email, code_booking):
        return self.repository.update_booking(booking_id, concert, user_name, user_email, code_booking)

    def delete_booking(self, booking_id):
        return self.repository.delete_booking(booking_id)