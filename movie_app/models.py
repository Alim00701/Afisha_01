from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    # movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def filtered_reviews(self):
        return self.reviews.filter(stars__gte=4)

    @property
    def reviews_count(self):
        return self.filtered_reviews.count()

    @property
    def rating(self):
        return 'f{CHOICES}'.average(self.rating)


CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    text = models.TextField(max_length=300)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES)

    def __str__(self):
        return self.text
