from Festy.presentation.serializers.serializers_booking import BookingSerializer
from Festy.metier.model.models import Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def booking_list(request):
    """
    List all bookings.
    """
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def booking_create(request):
    """
    Create a new booking.
    """
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def booking_detail(request, booking_id):
    """
    Retrieve a booking by its ID.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)

@api_view(['PUT'])
def booking_update(request, booking_id):
    """
    Update a booking by its ID.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)

    serializer = BookingSerializer(booking, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def booking_delete(request, booking_id):
    """
    Delete a booking by its ID.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.delete()
        return Response(status=204)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=404)