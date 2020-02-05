import os

import requests
from django.http import JsonResponse

API_KEY = os.getenv('OMDB_API_KEY', '')


def get_movies(request):
    movie_title = request.GET.get('movieTitle', '')
    url = f"http://omdbapi.com/?apikey={API_KEY}&s={movie_title}"
    response = requests.get(url).json()
    return JsonResponse(data=response)
