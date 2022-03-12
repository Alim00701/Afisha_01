from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField(max_length=300)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
