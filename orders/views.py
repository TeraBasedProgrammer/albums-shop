from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import generic

from .models import CartItem
from albums.models import Album


class CartView(LoginRequiredMixin, generic.ListView):
    template_name = 'orders/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)


def cart_item_create_view(request):
    album_pk = request.POST.get('album_pk')
    quantity = request.POST.get('quantity')
    album = Album.objects.get(pk=album_pk)

    CartItem.objects.get_or_create(user=request.user, album=album, quantity=quantity)
    return redirect('albums:album-detail', pk=album_pk)


def cart_item_remove_view(request):
    item_pk = request.POST.get('item_pk')

    CartItem.objects.filter(pk=item_pk).delete()
    return redirect('orders:cart')

