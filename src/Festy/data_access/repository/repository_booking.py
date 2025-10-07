from Festy.metier.model.models import Booking

class RepositoryBooking:

    def add_booking(self, user_name, user_email, concert, code_booking):
       reservation = Booking.objects.create(user_name=user_name, user_email=user_email, concert=concert, code_booking=code_booking)
       return reservation

    def get_booking_by_id(self, reservation_id):
        return Booking.objects.get(id=reservation_id)

    def get_all_booking(self):
        return Booking.objects.all()

    def update_booking(self, user_name, user_email, concert, code_booking, reservation_id):
        reservation = Booking.objects.get(id=reservation_id)
        reservation.user_name = user_name
        reservation.user_email = user_email
        reservation.concert = concert
        reservation.code_booking = code_booking
        reservation.save()
        return reservation

    def delete_booking(self, reservation_id):
        reservation = Booking.objects.get(id=reservation_id)
        reservation.delete()