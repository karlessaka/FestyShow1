from Festy.metier.services.service_booking import BookingService
from Festy.presentation.serializers.serializers_booking import BookingSerializer
from Festy.metier.model.models import Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

service = BookingService()

@api_view(['GET'])
def booking_list(request):
    """
    List all bookings.
    """
    try:
        bookings = service.get_all_bookings()
        serializer = BookingSerializer(bookings, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except Exception:
        logger.exception("Failed to list bookings")
        return Response({"success": False, "message": "Erreur lors de la récupération des réservations."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def booking_create(request):
    """
    Create a new booking.
    """
    serializer = BookingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        booking = service.create_booking(serializer.validated_data)
        out = BookingSerializer(booking)
        return Response({"success": True, "data": out.data}, status=status.HTTP_201_CREATED)
    except DRFValidationError as e:
        return Response({"success": False, "message": "Données invalides.", "errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        logger.exception("Database integrity error on create_booking")
        return Response({"success": False, "message": "Conflit en base de données."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        logger.exception("Unexpected error on create_booking")
        return Response({"success": False, "message": "Erreur serveur inattendue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def booking_detail(request, booking_id):
    """
    Retrieve a booking by its ID.
    """
    try:
        booking = service.get_booking_by_id(booking_id)
        serializer = BookingSerializer(booking)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Réservation introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        logger.exception("Failed to retrieve booking %s", booking_id)
        return Response({"success": False, "message": "Erreur lors de la récupération de la réservation."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def booking_update(request, booking_id):
    """
    Update a booking by its ID.
    """
    serializer = BookingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        updated = service.update_booking(booking_id, serializer.validated_data)
        out = BookingSerializer(updated)
        return Response({"success": True, "data": out.data}, status=status.HTTP_200_OK)
    except DRFValidationError as e:
        return Response({"success": False, "message": "Données invalides pour la mise à jour.", "errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Réservation à mettre à jour introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except IntegrityError:
        logger.exception("Database integrity error on update_booking")
        return Response({"success": False, "message": "Conflit en base de données lors de la mise à jour."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        logger.exception("Unexpected error on update_booking")
        return Response({"success": False, "message": "Erreur serveur inattendue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def booking_delete(request, booking_id):
    """
    Delete a booking by its ID.
    """
    try:
        service.delete_booking(booking_id)
        return Response({"success": True, "message": "Réservation supprimée avec succès."}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Réservation introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        logger.exception("Failed to delete booking %s", booking_id)
        return Response({"success": False, "message": "Erreur lors de la suppression de la réservation."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)