from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from .models import Album, Genre, Artist
from .forms import AlbumModelForm


# Alternative for get_context_data() method, retrieves genres and artists data
class ArtistsGenresData():
    def get_genres(self):
        return Genre.objects.get_ordered_by_title()
    
    def get_artists(self):
        return Artist.objects.get_ordered_by_title()




class AlbumListView(ArtistsGenresData, generic.ListView):
    model = Album
    template_name='albums_list.html'
    context_object_name = 'albums'


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'


class AlbumCreateView(generic.CreateView):
    template_name = "album_create.html"
    form_class = AlbumModelForm
    
    def get_success_url(self):
        return reverse("albums-list")


class AlbumDeleteView(generic.DeleteView):
    template_name = "album_delete.html"
    model = Album
    context_object_name = 'album'

    def get_success_url(self):
        return reverse("albums-list")

class AlbumUpdateView(generic.UpdateView):
    template_name = "album_update.html"
    form_class = AlbumModelForm
    model = Album

    def get_success_url(self):
        return reverse("albums-list")


class AlbumFilterView(ArtistsGenresData, generic.ListView):
    context_object_name = 'albums'
    template_name = 'albums_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        # Retrieving 'True' checkboxes' values from fort GET request
        genres_filters = self.request.GET.getlist("genre")
        artist_filters = self.request.GET.getlist("artist")

        kwargs = {}
        if genres_filters: 
            kwargs["genres__title__in"] = genres_filters

        if artist_filters:
            kwargs["artist__title__in"] = artist_filters

        return Album.objects.filter(**kwargs)


class AlbumSearchView(ArtistsGenresData, generic.ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'albums_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        object_list = Album.objects.filter(
            Q(title__icontains=query) |
            Q(artist__title__icontains=query)
            )
        return object_list
    