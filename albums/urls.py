from django.urls import path

from .views import (AlbumListView, AlbumDetailView , AlbumFilterView, AlbumSearchView, 
                    AlbumCreateView, AlbumUpdateView, AlbumDeleteView, GenreCreateView,
                    GenreUpdateView, GenreDeleteView, ArtistDeleteView, ArtistCreateView,
                    ArtistUpdateView)


urlpatterns = [
    # User endpoints (only albums)
    path('', AlbumListView.as_view(), name='albums-list'),
    path('filter/', AlbumFilterView.as_view(), name='albums-filter'),
    path('search/', AlbumSearchView.as_view(), name='albums-search'),
    path('<pk>/', AlbumDetailView.as_view(), name='album-detail'),
    
    # Admin endpoints

    # Albums
    path('create/', AlbumCreateView.as_view(), name='album-create'),
    path('<pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('<pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),

    # Genres
    path('genres/create/', GenreCreateView.as_view(), name='genre-create'),
    path('genres/<pk>/update/', GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<pk>/delete/', GenreDeleteView.as_view(), name='genre-delete'),

    # Artists
    path('artists/create/', ArtistCreateView.as_view(), name='artist-create'),
    path('artists/<pk>/update/', ArtistUpdateView.as_view(), name='artist-update'),
    path('artists/<pk>/delete/', ArtistDeleteView.as_view(), name='artist-delete'),
]