from Festy.presentation.serializers.serializers_artist import ArtistSerializer
from Festy.metier.services.service_artist import ArtistService
from Festy.metier.model.models import Artist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

service = ArtistService()


@api_view(["PUT"])
def artist_update(request, artist_id):
    """
    Update an existing artist.
    """
    serializer = ArtistSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        updated_artist = service.update_artist(artist_id, serializer.validated_data)
        out = ArtistSerializer(updated_artist)
        return Response({"success": True, "data": out.data}, status=status.HTTP_200_OK)
    except DRFValidationError as e:
        return Response(
            {
                "success": False,
                "message": "Données invalides pour la mise à jour.",
                "errors": e.detail,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    except ObjectDoesNotExist:
        return Response(
            {"success": False, "message": "Artiste introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except IntegrityError:
        logger.exception("Database integrity error on update_artist")
        return Response(
            {
                "success": False,
                "message": "Conflit en base de données lors de la mise à jour.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception:
        logger.exception("Unexpected error on update_artist")
        return Response(
            {"success": False, "message": "Erreur serveur inattendue."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def artist_create(request):
    """
    Create a new artist.
    """
    serializer = ArtistSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        artist = service.create_artist(serializer.validated_data)
        out = ArtistSerializer(artist)
        return Response({"success": True, "data": out.data}, status=status.HTTP_201_CREATED)
    except DRFValidationError as e:
        return Response(
            {"success": False, "message": "Données invalides.", "errors": e.detail},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except IntegrityError:
        logger.exception("Database integrity error on create_artist")
        return Response(
            {"success": False, "message": "Conflit en base de données."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception:
        logger.exception("Unexpected error on create_artist")
        return Response(
            {"success": False, "message": "Erreur serveur inattendue."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def artist_list(request):
    """
    List all artists.
    """
    try:
        artists = service.get_all_artists()
        serializer = ArtistSerializer(artists, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except Exception:
        logger.exception("Failed to list artists")
        return Response(
            {"success": False, "message": "Erreur lors de la récupération des artistes."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def artist_detail(request, artist_id):
    """
    Retrieve an artist by ID.
    """
    try:
        artist = service.get_artist_by_id(artist_id)
        serializer = ArtistSerializer(artist)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(
            {"success": False, "message": "Artiste introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        logger.exception("Failed to retrieve artist %s", artist_id)
        return Response(
            {"success": False, "message": "Erreur lors de la récupération de l'artiste."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["DELETE"])
def artist_delete(request, artist_id):
    """
    Delete an artist by ID.
    """
    try:
        service.delete_artist(artist_id)
        return Response(
            {"success": True, "message": "Artiste supprimé avec succès."}, status=status.HTTP_200_OK
        )
    except ObjectDoesNotExist:
        return Response(
            {"success": False, "message": "Artiste introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        logger.exception("Failed to delete artist %s", artist_id)
        return Response(
            {"success": False, "message": "Erreur lors de la suppression de l'artiste."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

