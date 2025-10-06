from Festy.presentation.serializers.serializers_concert import ConcertSerializer
from Festy.metier.model.models import Concert
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def concert_list(request):
#    List all concerts.
    concerts = Concert.objects.all()
    serializer = ConcertSerializer(concerts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def concert_create(request):
#    Create a new concert.
    serializer = ConcertSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def concert_detail(request, concert_id):
#    Retrieve a concert by ID.
    try:
        concert = Concert.objects.get(id=concert_id)
    except Concert.DoesNotExist:
        return Response(status=404)
    serializer = ConcertSerializer(concert)
    return Response(serializer.data)

@api_view(['PUT'])
def concert_update(request, concert_id):
#    Update a concert by ID.
    try:
        concert = Concert.objects.get(id=concert_id)
    except Concert.DoesNotExist:
        return Response(status=404)
    serializer = ConcertSerializer(concert, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
#    Delete a concert by ID.
def concert_delete(request, concert_id):
    try:
        concert = Concert.objects.get(id=concert_id)
    except Concert.DoesNotExist:
        return Response(status=404)
    concert.delete()
    return Response(status=204)
