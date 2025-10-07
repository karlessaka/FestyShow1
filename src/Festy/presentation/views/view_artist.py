from Festy.presentation.serializers.serializers_artist import ArtistSerializer
from Festy.metier.services.service_artist import ArtistService
from Festy.metier.model.models import Artist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

service = ArtistService()


@api_view(["PUT"])
def artist_update(request, artist_id):
    """
    Update an existing artist.
    """
    try:
        updated_artist = service.update_artist(artist_id, request.data)
        serializer = ArtistSerializer(updated_artist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def artist_create(request):
    """
    Create a new artist.
    """
    try:
        artist = service.create_artist(request.data)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def artist_list(request):
    """
    List all artists.
    """
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def artist_detail(request, artist_id):
    """
    Retrieve an artist by ID.
    """
    try:
        artist = Artist.objects.get(id=artist_id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    except Artist.DoesNotExist:
        return Response(status=404)


@api_view(["DELETE"])
def artist_delete(request, artist_id):
    """
    Delete an artist by ID.
    """
    try:
        artist = Artist.objects.get(id=artist_id)
        artist.delete()
        return Response(
            {"message": "user supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT
        )
    except Artist.DoesNotExist:
        return Response({"error": "artist not found"}, status=status.HTTP_404_NOT_FOUND)
