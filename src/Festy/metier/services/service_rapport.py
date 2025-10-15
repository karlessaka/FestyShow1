from Festy.data_access.repository.repository_rapport import RepositoryRapport

class RapportService:
    """
    Service pour gérer les rapports statistiques
    """
    
    def __init__(self):
        self.repository = RepositoryRapport()

    def get_booking_count_for_concert(self, concert_id):
        """
        Récupère le nombre de réservations pour un concert donné
        """
        return self.repository.get_booking_count_by_concert(concert_id)

    def get_bookings_list_for_concert(self, concert_id):
        """
        Récupère la liste des personnes ayant réservé pour un concert donné
        """
        return self.repository.get_bookings_by_concert(concert_id)

    def get_full_concert_report(self, concert_id):
        """
        Récupère le rapport complet d'un concert
        (infos + nombre de réservations + liste des personnes)
        """
        return self.repository.get_concert_full_report(concert_id)

    def get_all_concerts_statistics(self):
        """
        Récupère les statistiques de tous les concerts
        """
        return self.repository.get_all_concerts_statistics()