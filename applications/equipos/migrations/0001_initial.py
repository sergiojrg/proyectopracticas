# Generated by Django 4.0.2 on 2022-02-11 16:00

import ckeditor_uploader.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquiposModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre del Equipo')),
                ('marca', models.CharField(max_length=80, verbose_name='Marca')),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('ingeniero', models.CharField(max_length=120, verbose_name='Nombre del Ingeniero')),
                ('serie', models.CharField(max_length=80, verbose_name='Numero de Serie')),
                ('imagen', models.ImageField(upload_to='EquiposIMG')),
                ('terminos', models.TextField()),
                ('incluye', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=' ', null=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
    ]