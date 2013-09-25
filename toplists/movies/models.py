from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def is_terrible(self):
        return dislikes > likes

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return self.movie.title + ": " + self.text