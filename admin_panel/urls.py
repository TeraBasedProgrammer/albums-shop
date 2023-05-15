from django.urls import path

from .views import (MainView, AlbumsDataView, GenresDataView,
                    ArtistsDataView, AlbumsDataSearchView, UnconfirmedOrdersDataView,
                    ConfirmedOrdersDataView, UsersBlacklistView)

app_name = 'admin-panel'

urlpatterns = [
    path('', MainView.as_view(), name='main-page'),
    path('albums/', AlbumsDataView.as_view(), name='albums-data'),
    path('albums/search/', AlbumsDataSearchView.as_view(), name='albums-data-search'),
    path('genres/', GenresDataView.as_view(), name='genres-data'),
    path('artists/', ArtistsDataView.as_view(), name='artists-data'),
    path('blacklist/', UsersBlacklistView.as_view(), name='blacklist'),
    path('unconfirmed-orders/', UnconfirmedOrdersDataView.as_view(), name='unconfirmed-orders'),
    path('confirmed-orders/', ConfirmedOrdersDataView.as_view(), name='confirmed-orders'),
]