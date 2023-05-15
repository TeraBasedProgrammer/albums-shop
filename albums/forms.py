from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Album, Genre, Artist
from orders.models import CustomUser


class AlbumModelForm(forms.ModelForm):
    duration = forms.DurationField(widget=forms.TextInput(attrs={'placeholder': ''}))
    tracks = forms.CharField(label="Tracks",
                             widget=forms.Textarea())
    genres = forms.ModelMultipleChoiceField(
            widget=forms.SelectMultiple(),
            queryset=Genre.objects.get_ordered_by_title(),
            required=True,
        )
    artist = forms.ModelChoiceField(queryset=Artist.objects.get_ordered_by_title(),
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

    def clean_title(self):
        title = self.cleaned_data.get('title')
        album = Album.objects.filter(title__iexact=title).exists()
        if album:
            raise forms.ValidationError('Альбом з такою назвою вже існує')
        return title

    def clean(self):
        cleaned_data = super().clean()

        # Convert tracks string into list
        tracks = cleaned_data.get('tracks')
        tracks_list = [track for track in tracks.split('\r\n')]
        cleaned_data['tracks'] = tracks_list

        return cleaned_data


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        album = Genre.objects.filter(title__iexact=title).exists()
        if album:
            raise forms.ValidationError('Жанр з такою назвою вже існує')
        return title


class ArtistModelForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        album = Artist.objects.filter(title__iexact=title).exists()
        if album:
            raise forms.ValidationError('Артист з таким ім\'ям уже існує')
        return title


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "This username is already in use"
            )
        return username
