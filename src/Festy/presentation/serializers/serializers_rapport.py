from rest_framework import serializers

class BookingInfoSerializer(serializers.Serializer):
    """
    Serializer pour les informations d'une réservation
    """
    id = serializers.IntegerField()
    user_name = serializers.CharField()
    user_email = serializers.EmailField()
    code_booking = serializers.CharField()
    booking_date = serializers.DateTimeField()


class ConcertInfoSerializer(serializers.Serializer):
    """
    Serializer pour les informations d'un concert
    """
    id = serializers.IntegerField()
    title = serializers.CharField()
    artist_name = serializers.CharField()
    artist_style = serializers.CharField()
    location = serializers.CharField()
    date_time = serializers.DateTimeField()
    seats_available = serializers.IntegerField()


class BookingCountSerializer(serializers.Serializer):
    """
    Serializer pour le nombre de réservations d'un concert
    """
    concert_id = serializers.IntegerField()
    concert_title = serializers.CharField()
    artist_name = serializers.CharField()
    location = serializers.CharField()
    date_time = serializers.DateTimeField()
    booking_count = serializers.IntegerField()
    seats_available = serializers.IntegerField()
    seats_remaining = serializers.IntegerField()


class ConcertFullReportSerializer(serializers.Serializer):
    """
    Serializer pour le rapport complet d'un concert
    """
    concert_info = ConcertInfoSerializer()
    booking_count = serializers.IntegerField()
    seats_remaining = serializers.IntegerField()
    occupancy_rate = serializers.FloatField()
    bookings = BookingInfoSerializer(many=True)


class ConcertStatisticsSerializer(serializers.Serializer):
    """
    Serializer pour les statistiques d'un concert (vue synthétique)
    """
    concert_id = serializers.IntegerField()
    concert_title = serializers.CharField()
    artist_name = serializers.CharField()
    artist_style = serializers.CharField()
    location = serializers.CharField()
    date_time = serializers.DateTimeField()
    seats_available = serializers.IntegerField()
    booking_count = serializers.IntegerField()
    seats_remaining = serializers.IntegerField()
    occupancy_rate = serializers.FloatField()