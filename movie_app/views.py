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


@api_view(['GET', 'POST'])  # 1
def director_list_create_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'POST'])  # 2
def movie_list_create_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration,
                                     director_id=director_id)
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'POST'])  # 3
def review_list_create_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])  # 1
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'massage': 'Director removed'})
    else:
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])  # 2
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie removed'})
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])  # 4
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'message': 'Review removed'})
    else:
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET'])
def movie_rating_view(request):
    movie = Movie.objects.all()
    serializer = MoviesReviews(movie, many=False)
    return Response(data=serializer.data)
