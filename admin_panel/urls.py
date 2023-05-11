from django.urls import path

from .views import MainView, AlbumsDataView, GenresDataView, ArtistsDataView

app_name = 'admin-panel'

urlpatterns = [
    path('', MainView.as_view(), name='main-page'),
    path('albums/', AlbumsDataView.as_view(), name='albums-data'),
    path('genres/', GenresDataView.as_view(), name='genres-data'),
    path('artists/', ArtistsDataView.as_view(), name='artists-data'),
]