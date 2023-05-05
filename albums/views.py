from django.urls import reverse
from django.views import generic

from .models import Album
from .forms import AlbumModelForm


class AlbumListView(generic.ListView):
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
    

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse("albums-list")

class PostDeleteView(generic.DeleteView):
    template_name = "album_delete.html"
    model = Album
    context_object_name = 'album'

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if self.request.user != self.object.author:
    #             raise PermissionDenied()
    #     return super().dispatch(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse("profile", args=[self.request.user.pk])


# New
class PostUpdateView(generic.UpdateView):
    template_name = "album_update.html"
    # form_class = PostModelForm
    # model = Post

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if self.request.user != self.object.author:
    #             raise PermissionDenied()
    #     return super().dispatch(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse("profile", args=[self.request.user.pk])