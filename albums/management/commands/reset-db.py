from django.core.management.base import BaseCommand
from django.db.models import Model

import albums.models as models


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Retrieving all model classes of the project
        models_classes = dict([(name, cls) for name, cls in models.__dict__.items() if isinstance(cls, type) and issubclass(cls, Model)])

        # Cleaning all project's custom models 
        for key, value in models_classes.items():
            deleted_count, _ = value.objects.all().delete()
