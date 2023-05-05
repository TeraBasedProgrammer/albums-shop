from django import forms
from django.forms.widgets import DateInput

from .models import Album, Genre, Artist


class AlbumModelForm(forms.ModelForm):
    # TODO: add covnert function
    release_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    # TODO: Add validation
    duration = forms.DurationField()
    genres = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=[(genre.title, genre) for genre in Genre.objects.all().order_by('title')],
            required=True,
        )
    artist = forms.ChoiceField(choices=[(artist.title, artist) for artist in Artist.objects.all().order_by('title')],
                               required=True)


    class Meta:
        model = Album
        fields = (
            # TODO: add validation
            'title',
            'release_date',
            'duration',
            'image',
            'tracks',
            'price',
            'genres',
            'artist',
        )
