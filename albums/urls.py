from django.urls import path

from .views import AlbumListView, AlbumDetailView, AlbumCreateView


urlpatterns = [
    path('', AlbumListView.as_view(), name='albums-list'),
    path('create/', AlbumCreateView.as_view(), name='album-create'),
    path('<pk>/', AlbumDetailView.as_view(), name='album-detail'),
]