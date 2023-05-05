from django import forms
from django.forms.widgets import DateInput

from .models import Album, Genre, Artist


class AlbumModelForm(forms.ModelForm):
    release_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    duration = forms.DurationField(widget=forms.TextInput(attrs={'placeholder': ''}))
    tracks = forms.CharField(label="Tracks",
                                widget=forms.Textarea()) 
    genres = forms.ModelMultipleChoiceField(
            widget=forms.SelectMultiple(),
            queryset=Genre.objects.all(),
            required=True,
        )
    artist = forms.ModelChoiceField(queryset=Artist.objects.all().order_by('title'),
                               required=True)


    class Meta:
        model = Album
        fields = (
            'title',
            'release_date',
            'duration',
            'image',
            'tracks',
            'price',
            'genres',
            'artist',
        )

    def clean(self):
        cleaned_data = super().clean()

        # Convert date into proper format
        release_date = cleaned_data.get('release_date')
        cleaned_data['release_date'] = release_date.strftime('%B %d, %Y')


        # Convert tracks string into list
        tracks = cleaned_data.get('tracks')
        tracks_list = [track for track in tracks.split('\r\n')]
        cleaned_data['tracks'] = tracks_list

        return cleaned_data
        