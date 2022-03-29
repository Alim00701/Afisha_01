from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


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


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=30)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=16)
    description = serializers.CharField(min_length=2, max_length=77)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    # def validate_director_id(self, director_id):
    #     try:
    #         Director.objects.get(id=director_id)
    #     except Director.DoesNotExist:
    #         raise ValidationError('Director does not exist')

    def validate(self, attrs):
        try:
            Director.objects.get(id=attrs['director_id'])
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id {attrs["director_id"]} does not exist')
        return attrs


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2, max_length=300)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()
