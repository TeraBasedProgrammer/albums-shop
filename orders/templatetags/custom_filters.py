from django import template

register = template.Library()


@register.filter
def calculate_total(cart_items):
    total_price = sum([item.quantity * item.album.price for item in cart_items])
    return total_price
