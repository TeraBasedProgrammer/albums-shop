from .models import Genre, Artist


class ArtistsGenresDataMixin():
    def get_genres(self):
        return Genre.objects.get_ordered_by_title()
    
    def get_artists(self):
        return Artist.objects.get_ordered_by_title()
    
    def get_decades_range(self):
        return range(1950, 2021, 10)

    # Page size variable
    paginate_by = 10

# Get model name to dynamic template naming
class GetModelNameMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['model_name'] = context['model'].__class__.__name__.lower()
        except KeyError:
            # Retrieves model name from model form class name
            context['model_name'] = context['form'].__class__.__name__[:-9].lower() 
        return context




