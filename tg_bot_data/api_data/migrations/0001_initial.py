# Generated by Django 4.2.2 on 2023-06-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField(db_index=True, verbose_name='id в тг')),
                ('username', models.CharField(max_length=255, verbose_name='username в тг')),
            ],
            options={
                'db_table': 'TG_user',
            },
        ),
    ]
