from django.db import models

from .validators import validate_text


class GenreArtistManager(models.Manager):
    def get_ordered_by_title(self):
        return self.all().order_by('title')



class Artist(models.Model):
    title = models.CharField(max_length=75)

    objects = GenreArtistManager()
    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=75)
    
    objects = GenreArtistManager()
    
    def __str__(self) -> str:
        return self.title


class Album(models.Model):
    # General fields
    title = models.CharField(max_length=75, validators=[validate_text])
    release_date = models.CharField(max_length=25, blank=True)
    duration = models.CharField(max_length=10, blank=True)
    image = models.URLField()    
    tracks = models.JSONField()
    price = models.IntegerField()

    # One-to-many fields
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    # Many-to-many fields
    genres = models.ManyToManyField(Genre, db_table='AlbumsGenres')

    def __str__(self) -> str:
        return self.title 
    