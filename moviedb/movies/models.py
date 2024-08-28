from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year_of_release = models.IntegerField()
    user_ratings = models.FloatField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    technicians = models.ManyToManyField(Technician, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.name
