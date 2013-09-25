from models import Movie, Comment

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def movie_list(request):
    list_of_all_movies = Movie.objects.all()
    context = {'movies_list': list_of_all_movies}
    return render(request, 'movies/movies_list.html', context)

def add_movie(request):
    newmovie = Movie(title=request.POST['movie_title'])
    newmovie.save()
    return HttpResponseRedirect('/movies')

def movie(request, movie_id):
    return HttpResponse("this is where you see movie number " + movie_id + " and all it's comments")

def add_comment(request, movie_id):
    return HttpResponse("adding comment to movie " + movie_id)