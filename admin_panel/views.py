from typing import Any, Dict

from django.views import generic
from django.urls import reverse 

from albums.models import Album, Genre, Artist


class MainView(generic.TemplateView):
    template_name = 'admin_panel/main.html'


class AlbumsDataView(generic.ListView):
    template_name = 'admin_panel/albums.html'
    queryset = Album.objects.all()
    context_object_name = 'albums'
    
    paginate_by = 20
    

class GenresDataView(generic.ListView):
    template_name = 'admin_panel/genres.html'
    queryset = Genre.objects.all()
    context_object_name = 'genres'


class ArtistsDataView(generic.ListView):
    template_name = 'admin_panel/artists.html'
    queryset = Artist.objects.all()
    context_object_name = 'artists'


