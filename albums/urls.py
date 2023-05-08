from django.urls import path

from .views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumDeleteView, AlbumUpdateView, AlbumFilterView, AlbumSearchView


urlpatterns = [
    path('', AlbumListView.as_view(), name='albums-list'),
    path('filter/', AlbumFilterView.as_view(), name='albums-filter'),
    path('search/', AlbumSearchView.as_view(), name='albums-search'),
    path('create/', AlbumCreateView.as_view(), name='album-create'),
    path('<pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('<pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('<pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]