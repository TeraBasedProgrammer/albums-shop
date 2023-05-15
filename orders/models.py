from django.contrib.auth.models import User
from django.db import models

from albums.models import Album


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    albums = models.ManyToManyField(db_table='OrderAlbum', to=Album)
    created_at = models.DateTimeField(auto_now_add=True)

