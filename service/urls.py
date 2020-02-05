from django.urls import path

from service.views import get_movies

urlpatterns = [
    path('get-movies/', get_movies, name='get-movies'),
]
