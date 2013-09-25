# Create your views here.
from django.http import HttpResponse

def movie_list(request):
    return HttpResponse("this is the list of all movies")

def add_movie(request):
    return HttpResponse("adding movie")

def movie(request, movie_id):
    return HttpResponse("this is where you see movie number " + movie_id + " and all it's comments")

def add_comment(request, movie_id):
    return HttpResponse("adding comment to movie " + movie_id)

def like(request, movie_id):
    return HttpResponse("you liked movie " + movie_id)

def dislike(request, movie_id):
    return HttpResponse("you disliked movie " + movie_id)