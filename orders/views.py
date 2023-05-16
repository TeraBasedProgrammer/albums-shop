from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic


from .models import CartItem, Order, CustomUser
from albums.models import Album


class CartView(LoginRequiredMixin, generic.ListView):
    template_name = 'orders/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['unpaid_order'] = Order.objects.filter(user=self.request.user, is_paid=False)
        return context


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
    if request.user != order.user:
        return HttpResponseForbidden()

    if order.is_paid:
        return redirect('albums:albums-list')

    return render(request, 'orders/order_pay.html', context={'pk': pk})


def order_success_pay_view(request, pk):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        order = get_object_or_404(Order, pk=pk)
        order.is_paid = True
        order.save()

        # Clean cart
        CartItem.objects.filter(user=request.user).delete()
        return render(request, 'orders/order_success_pay.html')
    else:
        return HttpResponseNotAllowed(['POST'])


def order_confirm_view(request, pk):
    if request.method == 'POST':
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        order = get_object_or_404(Order, pk=pk)
        order.is_confirmed = True
        order.save()

        return redirect('admin-panel:unconfirmed-orders')
    else:
        return HttpResponseNotAllowed(['POST'])


def order_discard_view(request, pk):
    if request.method == 'POST':
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        order = get_object_or_404(Order, pk=pk)
        order.delete()

        return redirect('admin-panel:unconfirmed-orders')
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


def user_ban_view(request, username):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        user = get_object_or_404(CustomUser, username=username)
        user.is_banned = True
        user.save()
        return redirect('admin-panel:unconfirmed-orders')
    else:
        return HttpResponseNotAllowed(['POST'])


def user_unban_view(request, username):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        user = get_object_or_404(CustomUser, username=username)
        user.is_banned = False
        user.save()
        return redirect('admin-panel:blacklist')
    else:
        return HttpResponseNotAllowed(['POST'])
