from Festy.presentation.serializers.serializers_artist import ArtistSerializer
from Festy.metier.model.models import Artist
from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def artist_list(request):
    """
    List all artists.
    """
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def artist_create(request):
    """
    Create a new artist.
    """
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)