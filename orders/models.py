from django.contrib.auth.models import AbstractUser, User
from django.db import models

from albums.models import Album


class CustomUser(AbstractUser):
    is_banned = models.BooleanField(default=False)


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    albums = models.ManyToManyField(db_table='OrderAlbum', to=Album)
    created_at = models.DateTimeField(auto_now_add=True)

