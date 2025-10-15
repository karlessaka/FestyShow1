from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Festy.metier.services.service_rapport import RapportService
from Festy.presentation.serializers.serializers_rapport import *

# Création d'une instance du service
service = RapportService()


@api_view(['GET'])
def rapport_booking_count(request, concert_id):
    """
    Retourne le nombre de réservations pour un concert donné
    Endpoint: GET /rapport/booking-count/<concert_id>/
    
    Réponse :
    {
        "concert_id": 1,
        "concert_title": "Rock Festival",
        "artist_name": "John Doe",
        "location": "Paris",
        "date_time": "2025-12-25T20:00:00Z",
        "booking_count": 25,
        "seats_available": 150,
        "seats_remaining": 125
    }
    """
    data = service.get_booking_count_for_concert(concert_id)
    
    if data is None:
        return Response(
            {"error": "Concert not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = BookingCountSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def rapport_bookings_list(request, concert_id):
    """
    Retourne la liste des personnes ayant réservé pour un concert donné
    Endpoint: GET /rapport/bookings-list/<concert_id>/
    
    Réponse :
    [
        {
            "id": 1,
            "user_name": "Jean Dupont",
            "user_email": "jean@example.com",
            "code_booking": "ABC123",
            "booking_date": "2025-10-01T10:00:00Z"
        },
        ...
    ]
    """
    data = service.get_bookings_list_for_concert(concert_id)
    
    if data is None:
        return Response(
            {"error": "Concert not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = BookingInfoSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def rapport_concert_full(request, concert_id):
    """
    Retourne le rapport complet pour un concert donné
    (informations du concert + nombre de réservations + liste des personnes)
    Endpoint: GET /rapport/concert-full/<concert_id>/
    
    Réponse :
    {
        "concert_info": {
            "id": 1,
            "title": "Rock Festival",
            "artist_name": "John Doe",
            "artist_style": "ROCK",
            "location": "Paris",
            "date_time": "2025-12-25T20:00:00Z",
            "seats_available": 150
        },
        "booking_count": 25,
        "seats_remaining": 125,
        "occupancy_rate": 16.67,
        "bookings": [...]
    }
    """
    data = service.get_full_concert_report(concert_id)
    
    if data is None:
        return Response(
            {"error": "Concert not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = ConcertFullReportSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def rapport_all_concerts(request):
    """
    Retourne les statistiques pour tous les concerts
    Endpoint: GET /rapport/all-concerts/
    
    Réponse :
    [
        {
            "concert_id": 1,
            "concert_title": "Rock Festival",
            "artist_name": "John Doe",
            "artist_style": "ROCK",
            "location": "Paris",
            "date_time": "2025-12-25T20:00:00Z",
            "seats_available": 150,
            "booking_count": 25,
            "seats_remaining": 125,
            "occupancy_rate": 16.67
        },
        ...
    ]
    """
    data = service.get_all_concerts_statistics()
    
    serializer = ConcertStatisticsSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)