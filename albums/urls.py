from django.urls import path

from .views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumDeleteView


urlpatterns = [
    path('', AlbumListView.as_view(), name='albums-list'),
    path('create/', AlbumCreateView.as_view(), name='album-create'),
    path('<pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('<pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]