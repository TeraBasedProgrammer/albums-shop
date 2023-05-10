from .models import Genre, Artist

class ArtistsGenresDataMixin():
    def get_genres(self):
        return Genre.objects.get_ordered_by_title()
    
    def get_artists(self):
        return Artist.objects.get_ordered_by_title()
    
    def get_decades_range(self):
        return range(1950, 2021, 10)

    paginate_by = 10
