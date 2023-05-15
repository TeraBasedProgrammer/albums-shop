from django.urls import path

from .views import (CartView, cart_item_create_view, cart_item_remove_view,
                    order_create_view, order_pay_view, order_success_pay_view,
                    order_confirm_view, order_discard_view, user_ban_view, user_unban_view)

app_name = 'orders'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', cart_item_create_view, name='cart-item-create'),
    path('delete/', cart_item_remove_view, name='cart-item-remove'),
    path('users/ban/<int:pk>/', user_ban_view, name='user-ban'),
    path('users/unban/<int:pk>/', user_unban_view, name='user-unban'),
    path('orders/', order_create_view, name='order-create'),
    path('orders/<int:pk>/pay/', order_pay_view, name='order-pay'),
    path('orders/<int:pk>/confirm/', order_confirm_view, name='order-confirm'),
    path('orders/<int:pk>/discard/', order_discard_view, name='order-discard'),
    path('orders/<int:pk>/pay/success/', order_success_pay_view, name='order-success-pay'),
]
