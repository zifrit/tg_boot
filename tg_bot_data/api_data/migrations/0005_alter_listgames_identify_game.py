# Generated by Django 4.2.2 on 2023-06-27 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_data', '0004_remove_listgames_players_listgames_identify_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listgames',
            name='identify_game',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)], verbose_name='id game'),
        ),
    ]
