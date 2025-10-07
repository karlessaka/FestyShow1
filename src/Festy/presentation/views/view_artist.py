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



@api_view(['GET'])
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
    

@api_view(['PUT'])
def artist_update(request, artist_id):
    """
    Update an existing artist.
    """
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return Response(status=404)

    serializer = ArtistSerializer(artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def artist_delete(request, artist_id):
    """
    Delete an artist by ID.
    """
    try:
        artist = Artist.objects.get(id=artist_id)
        artist.delete()
        return Response(status=204)
    except Artist.DoesNotExist:
        return Response(status=404)
    