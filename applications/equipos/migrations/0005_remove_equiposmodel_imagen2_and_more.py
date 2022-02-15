# Generated by Django 4.0.2 on 2022-02-15 22:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_equiposmodel_imagen2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equiposmodel',
            name='imagen2',
        ),
        migrations.AlterField(
            model_name='equiposmodel',
            name='imagen',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen'),
        ),
    ]
