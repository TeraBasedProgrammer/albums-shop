# Generated by Django 4.1.7 on 2023-05-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_alter_album_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='count',
            field=models.IntegerField(default=10000),
        ),
    ]
