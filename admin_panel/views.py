from typing import Any, Dict

from django.views import generic
from django.urls import reverse 

from albums.models import Album, Genre, Artist


class MainView(generic.TemplateView):
    template_name = 'admin_panel/main.html'

