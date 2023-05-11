from django.views import generic

from albums.models import Album, Genre, Artist
from albums.views import AlbumSearchView
from albums.mixins import  AdminRequiredMixin


class MainView(AdminRequiredMixin, generic.TemplateView):
    template_name = 'admin_panel/main.html'


class AlbumsDataView(AdminRequiredMixin, generic.ListView):
    template_name = 'admin_panel/albums.html'
    queryset = Album.objects.all()
    context_object_name = 'albums'
    
    paginate_by = 20


class AlbumsDataSearchView(AdminRequiredMixin, AlbumSearchView):
    template_name = 'admin_panel/albums.html'
    

class GenresDataView(AdminRequiredMixin, generic.ListView):
    template_name = 'admin_panel/genres.html'
    queryset = Genre.objects.get_ordered_by_title()
    context_object_name = 'genres'


class ArtistsDataView(AdminRequiredMixin, generic.ListView):
    template_name = 'admin_panel/artists.html'
    queryset = Artist.objects.get_ordered_by_title()
    context_object_name = 'artists'


