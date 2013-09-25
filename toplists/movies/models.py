from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    movie = models.ForeignKey(Movie)