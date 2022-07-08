from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor, through="Role")

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')