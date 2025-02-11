from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'mainMovie.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'Movieetail.html', {'movie': movie})