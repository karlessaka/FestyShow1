from Festy.metier.model.models import Booking, Concert

class RepositoryRapport:
    """
    Repository pour les rapports statistiques
    """

    def get_booking_count_by_concert(self, concert_id):
        """
        Retourne le nombre de réservations pour un concert donné
        """
        try:
            concert = Concert.objects.get(id=concert_id)
            booking_count = Booking.objects.filter(concert=concert).count()
            return {
                'concert_id': concert_id,
                'concert_title': concert.title,
                'artist_name': concert.artist.Full_name,
                'location': concert.location,
                'date_time': concert.date_time,
                'booking_count': booking_count,
                'seats_available': concert.seats_available,
                'seats_remaining': concert.seats_available - booking_count
            }
        except Concert.DoesNotExist:
            return None

    def get_bookings_by_concert(self, concert_id):
        """
        Retourne la liste des personnes ayant réservé pour un concert donné
        """
        try:
            concert = Concert.objects.get(id=concert_id)
            bookings = Booking.objects.filter(concert=concert)
            
            booking_list = []
            for booking in bookings:
                booking_list.append({
                    'id': booking.id,
                    'user_name': booking.user_name,
                    'user_email': booking.user_email,
                    'code_booking': booking.code_booking,
                    'booking_date': booking.booking_date
                })
            
            return booking_list
        except Concert.DoesNotExist:
            return None

    def get_concert_full_report(self, concert_id):
        """
        Retourne un rapport complet : 
        - Informations du concert
        - Nombre de réservations
        - Liste des personnes ayant réservé
        """
        try:
            concert = Concert.objects.get(id=concert_id)
            bookings = Booking.objects.filter(concert=concert)
            
            booking_list = []
            for booking in bookings:
                booking_list.append({
                    'id': booking.id,
                    'user_name': booking.user_name,
                    'user_email': booking.user_email,
                    'code_booking': booking.code_booking,
                    'booking_date': booking.booking_date
                })
            
            booking_count = len(booking_list)
            
            return {
                'concert_info': {
                    'id': concert.id,
                    'title': concert.title,
                    'artist_name': concert.artist.Full_name,
                    'artist_style': concert.artist.style,
                    'location': concert.location,
                    'date_time': concert.date_time,
                    'seats_available': concert.seats_available
                },
                'booking_count': booking_count,
                'seats_remaining': concert.seats_available - booking_count,
                'occupancy_rate': round((booking_count / concert.seats_available) * 100, 2) if concert.seats_available > 0 else 0,
                'bookings': booking_list
            }
        except Concert.DoesNotExist:
            return None

    def get_all_concerts_statistics(self):
        """
        Retourne les statistiques pour tous les concerts
        """
        concerts = Concert.objects.all()
        statistics = []
        
        for concert in concerts:
            booking_count = Booking.objects.filter(concert=concert).count()
            seats_remaining = concert.seats_available - booking_count
            occupancy_rate = round((booking_count / concert.seats_available) * 100, 2) if concert.seats_available > 0 else 0
            
            statistics.append({
                'concert_id': concert.id,
                'concert_title': concert.title,
                'artist_name': concert.artist.Full_name,
                'artist_style': concert.artist.style,
                'location': concert.location,
                'date_time': concert.date_time,
                'seats_available': concert.seats_available,
                'booking_count': booking_count,
                'seats_remaining': seats_remaining,
                'occupancy_rate': occupancy_rate
            })
        
        return statistics