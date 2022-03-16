from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title director reviews reviews_count average_rating'.split()

    def get_reviews(self, movie):
        # filtered_reviews = Review.objects.filter(movie=movie, stars__gte=4)
        filtered_reviews = movie.reviews.filter(stars__gte=4)
        return ReviewSerializer(filtered_reviews, many=True).data

    def get_reviews_count(self, movie):
        return movie.reviews.filter(stars__gte=4).count()


class MoviesReviews(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title average_rating'.split()
