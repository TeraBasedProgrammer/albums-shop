from django.db import models

class Artist(models.Model):
    title = models.CharField(max_length=75)


class Genre(models.Model):
    title = models.CharField(max_length=75)


class Album(models.Model):
    # General fields
    title = models.CharField(max_length=75)
    release_date = models.CharField(max_length=25)
    duration = models.TimeField()
    image = models.URLField()
    tracks = models.JSONField()

    # One-to-many fields
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    # Many-to-many fields
    genres = models.ManyToManyField(Genre, db_table='AlbumsGenres')

    
# {
#     "title": "The Piper at the Gates of Dawn",
#     "artist": "Pink Floyd",
#     "release-date": "August 5, 1967",
#     "duration": "41:54",
#     "image": "https://rovimusic.rovicorp.com/image.jpg?c=D9T8Ace0Aln_sPy-3GFMmVWnbEN5fCjifro6xhIBuB4=&f=4",
#     "styles": [
#         "Art Rock",
#         "British Invasion",
#         "British Psychedelia",
#         "Prog-Rock",
#         "Psychedelic/Garage",
#         "Album Rock"
#     ],
#     "tracks": [
#         "Astronomy Domine",
#         "Lucifer Sam",
#         "Matilda Mother",
#         "Flaming",
#         "Pow R. Toc. H",
#         "Take Up Thy Stethoscope and Walk",
#         "Interstellar Overdrive",
#         "The Gnome",
#         "Chapter 24",
#         "The Scarecrow",
#         "Bike"
#     ]
# },