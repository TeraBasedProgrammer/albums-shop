from django.urls import path

from .views import MainView, AlbumsDataView, GenresDataView, ArtistsDataView, AlbumsDataSearchView

app_name = 'admin-panel'

urlpatterns = [
    path('', MainView.as_view(), name='main-page'),
    path('albums/', AlbumsDataView.as_view(), name='albums-data'),
    path('albums/search/', AlbumsDataSearchView.as_view(), name='albums-data-search'),
    path('genres/', GenresDataView.as_view(), name='genres-data'),
    path('artists/', ArtistsDataView.as_view(), name='artists-data'),
]