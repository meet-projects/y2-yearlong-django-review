# always remember to import your models so you can use them
from models import Movie, Comment

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def movie_list(request):
    list_of_all_movies = Movie.objects.all()
    context = {'movies_list': list_of_all_movies}
    # when you render, always pass a context as a dictionary
    # the way it is written here, movies_list.html can now
    # use a variable called "movies_list"
    return render(request, 'movies/movies_list.html', context)

# an example of how to process form submission
def add_movie(request):
    newmovie = Movie(title=request.POST['movie_title'])
    # when making new objects, always remember to save them
    newmovie.save()
    return HttpResponseRedirect('/movies')

def movie(request, movie_id):
    # find the single movie that corresponds to primary key (id)
    # equal to the movie_id from the URL
    # because the .filter() method returns a list 
    one_movie = Movie.objects.filter(pk = movie_id)[0]
    list_of_comments = Comment.objects.filter(movie=one_movie)
    context = {'movie': one_movie, 'comment_list': list_of_comments}
    return render(request, 'movies/movie.html', context)

def add_comment(request, movie_id):
    movie_to_add_comment_to = Movie.objects.filter(pk = movie_id)[0]
    new_comment = Comment(text=request.POST['comment_text'], movie=movie_to_add_comment_to)
    new_comment.save()
    return HttpResponseRedirect('/movies/' + movie_id + '/')