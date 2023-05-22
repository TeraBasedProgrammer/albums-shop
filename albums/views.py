from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from .models import Album, Genre, Artist
from .forms import AlbumModelForm, ArtistModelForm, GenreModelForm, CustomUserCreationForm
from .mixins import ArtistsGenresDataMixin, GetModelNameMixin, AdminRequiredMixin
from orders.models import CartItem, Order


# Additional view to add context data to filter sidebar
# User views

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse("login")


class AlbumListView(ArtistsGenresDataMixin, generic.ListView):
    model = Album
    template_name = 'albums/albums_list.html'
    context_object_name = 'albums'


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_item'] = CartItem.objects.filter(user=self.request.user, album__pk=context['album'].pk)
        return context


class AlbumFilterView(ArtistsGenresDataMixin, generic.ListView):
    context_object_name = 'albums'
    template_name = 'albums/albums_list.html'

    def get_queryset(self) -> QuerySet[Any]:

        # Retrieving 'True' checkboxes' values from fort GET request
        genres_filters = self.request.GET.getlist("genre")
        artist_filters = self.request.GET.getlist("artist")
        decade_filters = self.request.GET.getlist("decades")

        sort_query = self.request.GET.get('sort_by')

        # Condition to prevent hand-written query parametrs in link
        allowed_sort_queries = ['price', '-price', 'release_date', '-release_date']
        if sort_query not in allowed_sort_queries:
            sort_query = None

        kwargs = {}
        if genres_filters: 
            kwargs["genres__title__in"] = genres_filters

        if artist_filters:
            kwargs["artist__title__in"] = artist_filters
        
        # if decade_filters:
        #     kwargs["release_date__range"] =  (decade_filters[0], int(decade_filters[0]) + 9)

        args = []

        # Multiple decades filtering
        if decade_filters:
            q = Q()
            for decade in decade_filters:
                start_year = decade
                end_year = int(decade) + 9
                q |= Q(release_date__range=(start_year, end_year))
                
            args.append(q) 

        print(args)
        print(kwargs)
        album = Album.objects.filter(
            *args,
            **kwargs).order_by('pk' if not sort_query else sort_query).distinct()
        return album


class AlbumSearchView(ArtistsGenresDataMixin, generic.ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'albums/albums_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")

        object_list = Album.objects.filter(
            Q(title__icontains=query) |
            Q(artist__title__icontains=query)
            ).order_by('artist', 'title')
        
        return object_list
    
# Admin views


# Albums
class AlbumCreateView(AdminRequiredMixin, GetModelNameMixin, generic.CreateView):
    template_name = "albums/album_create.html"
    form_class = AlbumModelForm
    
    def get_success_url(self):
        return reverse("admin-panel:albums-data")


class AlbumDeleteView(AdminRequiredMixin, GetModelNameMixin, generic.DeleteView):
    template_name = "albums/album_delete.html"
    model = Album
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:albums-data")


class AlbumUpdateView(AdminRequiredMixin, GetModelNameMixin, generic.UpdateView):
    template_name = "albums/album_update.html"
    form_class = AlbumModelForm
    model = Album
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:albums-data")


# Genres
class GenreCreateView(AdminRequiredMixin, GetModelNameMixin, generic.CreateView):
    template_name = "albums/album_create.html"
    form_class = GenreModelForm
    
    def get_success_url(self):
        return reverse("admin-panel:genres-data")


class GenreDeleteView(AdminRequiredMixin, GetModelNameMixin, generic.DeleteView):
    template_name = "albums/album_delete.html"
    model = Genre
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:genres-data")


class GenreUpdateView(AdminRequiredMixin, GetModelNameMixin, generic.UpdateView):
    template_name = "albums/album_update.html"
    form_class = GenreModelForm
    model = Genre
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:genres-data")


# Artists
class ArtistCreateView(AdminRequiredMixin, GetModelNameMixin, generic.CreateView):
    template_name = "albums/album_create.html"
    form_class = ArtistModelForm
    
    def get_success_url(self):
        return reverse("admin-panel:artists-data")


class ArtistDeleteView(AdminRequiredMixin, GetModelNameMixin, generic.DeleteView):
    template_name = "albums/album_delete.html"
    model = Artist
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:artists-data")


class ArtistUpdateView(AdminRequiredMixin, GetModelNameMixin, generic.UpdateView):
    template_name = "albums/album_update.html"
    form_class = ArtistModelForm
    model = Artist
    context_object_name = 'model'

    def get_success_url(self):
        return reverse("admin-panel:artists-data")
    