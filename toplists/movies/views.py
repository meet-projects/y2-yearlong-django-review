# Create your views here.
from django.http import HttpResponse

def movie_list(request):
    return HttpResponse("this is the list of all movies")

def movie(request):
    return HttpResponse("this is where you see one movie and all it's comments")

def add_movie(request):
    return HttpResponse("adding movie")

def add_comment(request):
    return HttpResponse("adding comment")