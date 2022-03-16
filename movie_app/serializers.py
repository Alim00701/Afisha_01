from rest_framework import serializers
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_reviews(self, movie):
        # filtered_reviews = Review.objects.filter(movie=movie, stars__gte=4)
        filtered_reviews = movie.reviews.filter(stars__gte=4)
        return ReviewSerializer(filtered_reviews, many=True).data

    def get_reviews_count(self, movie):
        return movie.reviews.filter(stars__gte=4).count()
