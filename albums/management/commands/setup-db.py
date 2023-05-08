import json
from datetime import date
import random

from django.core.management.base import BaseCommand
from albums.models import Album, Genre, Artist


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('albums-v2.json', 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        for album in data:
            # Skip 'not found' albums
            if len(album) == 1:
                continue
            current_artist = Artist.objects.get_or_create(title=album['artist'])
            current_genres = [Genre.objects.get_or_create(title=genre) for genre in album['styles']]
            album = Album.objects.create(title=album['title'],
                                artist=current_artist[0],
                                release_date=album['release-date'][-4:],
                                price=random.randint(1000, 5000),
                                duration=album['duration'],
                                image=album['image'],
                                tracks=album['tracks'])
            album.genres.set([genre[0] for genre in current_genres])
        