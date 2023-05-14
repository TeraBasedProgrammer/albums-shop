from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from albums.models import Album


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


# @receiver(post_save, sender=User)
# def create_cart(sender, instance, created, **kwargs):
#     if created:
#         CartItem.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_cart(sender, instance, **kwargs):
#     instance.cart.save()


class Order(models.Model):
    ...
