# Generated by Django 4.2.2 on 2023-06-27 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_data', '0006_alter_tguser_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listgames',
            name='identify_game',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)], verbose_name='id game'),
        ),
    ]
