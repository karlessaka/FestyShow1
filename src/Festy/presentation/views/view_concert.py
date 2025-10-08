from Festy.metier.services.service_concert import ConcertService
from Festy.presentation.serializers.serializers_concert import ConcertSerializer
from Festy.metier.model.models import Concert
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

service = ConcertService()


@api_view(['GET'])
def concert_list(request):
    # List all concerts.
    try:
        concerts = service.get_all_concerts()
        serializer = ConcertSerializer(concerts, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except Exception:
        logger.exception("Failed to list concerts")
        return Response({"success": False, "message": "Erreur lors de la récupération des concerts."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     

@api_view(['POST'])
def concert_create(request):
    # Create a new concert.
    serializer = ConcertSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        concert = service.create_concert(serializer.validated_data)
        out = ConcertSerializer(concert)
        return Response({"success": True, "data": out.data}, status=status.HTTP_201_CREATED)
    except DRFValidationError as e:
        return Response({"success": False, "message": "Données invalides.", "errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        logger.exception("Database integrity error on create_concert")
        return Response({"success": False, "message": "Conflit en base de données."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        logger.exception("Unexpected error on create_concert")
        return Response({"success": False, "message": "Erreur serveur inattendue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['GET'])
def concert_detail(request, concert_id):
    # Retrieve a concert by ID.
    try:
        concert = service.get_concert_by_id(concert_id)
        serializer = ConcertSerializer(concert)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Concert introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        logger.exception("Failed to retrieve concert %s", concert_id)
        return Response({"success": False, "message": "Erreur lors de la récupération du concert."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



@api_view(['PUT'])
def concert_update(request, concert_id):
    # Update a concert by ID.
    serializer = ConcertSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        updated = service.update_concert(concert_id, serializer.validated_data)
        out = ConcertSerializer(updated)
        return Response({"success": True, "data": out.data}, status=status.HTTP_200_OK)
    except DRFValidationError as e:
        return Response({"success": False, "message": "Données invalides pour la mise à jour.", "errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Concert à mettre à jour introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except IntegrityError:
        logger.exception("Database integrity error on update_concert")
        return Response({"success": False, "message": "Conflit en base de données lors de la mise à jour."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        logger.exception("Unexpected error on update_concert")
        return Response({"success": False, "message": "Erreur serveur inattendue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
# Delete a concert by ID.
def concert_delete(request, concert_id):
    try:
        service.delete_concert(concert_id)
        return Response({"success": True, "message": "Concert supprimé avec succès."}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"success": False, "message": "Concert introuvable."}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        logger.exception("Failed to delete concert %s", concert_id)
        return Response({"success": False, "message": "Erreur lors de la suppression du concert."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
