from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return self.movie.title + ": " + self.text