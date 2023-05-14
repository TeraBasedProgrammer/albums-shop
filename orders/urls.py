from django.urls import path

from .views import CartView, cart_item_create_view, cart_item_remove_view

app_name = 'orders'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', cart_item_create_view, name='cart-item-create'),
    path('delete/', cart_item_remove_view, name='cart-item-remove'),
]
