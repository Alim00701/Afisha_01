from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
"---------------------------------------------"
from movie_app.serializers import DirectorSerializer, MoviesReviews
from movie_app.models import Director
"---------------------------------------------"
from movie_app.serializers import MovieSerializer
from movie_app.models import Movie
"---------------------------------------------"
from movie_app.serializers import ReviewSerializer
from movie_app.models import Review


@api_view(['GET'])
def director_list_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_rating_view(request):
    movie = Movie.objects.all()
    serializer = MoviesReviews(movie, many=False)
    return Response(data=serializer.data)
