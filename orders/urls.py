from django.urls import path

from .views import (CartView,
                    cart_item_create_view,
                    cart_item_remove_view,
                    order_create_view,
                    order_pay_view,
                    order_success_pay_view)

app_name = 'orders'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', cart_item_create_view, name='cart-item-create'),
    path('delete/', cart_item_remove_view, name='cart-item-remove'),
    path('orders/', order_create_view, name='order-create'),
    path('orders/<int:pk>/pay/', order_pay_view, name='order-pay'),
    path('orders/<int:pk>/pay/success/', order_success_pay_view, name='order-success-pay'),

]
