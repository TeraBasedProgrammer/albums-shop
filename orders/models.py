from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from albums.models import Album


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        primary_key=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    is_banned = models.BooleanField(default=False)


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    total_price = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    albums = models.ManyToManyField(db_table='OrderAlbum', to=Album)
    created_at = models.DateTimeField(auto_now_add=True)

