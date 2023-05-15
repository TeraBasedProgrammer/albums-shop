from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic


from .models import CartItem, Order
from albums.models import Album


class CartView(LoginRequiredMixin, generic.ListView):
    template_name = 'orders/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)


def order_create_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        total_price = request.POST.get('total_price')

        cart_items = [item['album_id'] for item in CartItem.objects.filter(user=request.user).values('album_id')]
        albums = Album.objects.filter(pk__in=cart_items)

        order = Order.objects.create(user=request.user, total_price=total_price)
        order.albums.set(albums)

        return redirect('orders:order-pay', pk=order.pk)
    else:
        return HttpResponseNotAllowed(['POST'])


def order_pay_view(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    order = get_object_or_404(Order, pk=pk)
    print(order.is_paid)
    if order.is_paid:
        return redirect('albums:albums-list')

    return render(request, 'orders/order_pay.html', context={'pk': pk})


def order_success_pay_view(request, pk):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=pk)
        order.is_paid = True
        order.save()
        return render(request, 'orders/order_success_pay.html')
    else:
        return HttpResponseNotAllowed(['POST'])


def cart_item_create_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        album_pk = request.POST.get('album_pk')
        quantity = request.POST.get('quantity')
        album = get_object_or_404(Album, pk=album_pk)

        CartItem.objects.get_or_create(user=request.user, album=album, quantity=quantity)
        return redirect('albums:album-detail', pk=album_pk)
    else:
        return HttpResponseNotAllowed(['POST'])




def cart_item_remove_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        item_pk = request.POST.get('item_pk')

        CartItem.objects.filter(user=request.user, pk=item_pk).delete()
        return redirect('orders:cart')
    else:
        return HttpResponseNotAllowed(['POST'])

