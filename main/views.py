from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Movie
from .serializers import FilmsSerializer

# Create your views here.
@api_view(['GET'])
def film_list_view(request):
    movies = Movie.objects.all()
    serializer = FilmsSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def film_detail_view(request, id):
    try:
        product = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={
                "ERROR": "Movie does not exist!"
            }
            )
    serializer = FilmsSerializer(product, many=False)
    return Response(data=serializer.data)