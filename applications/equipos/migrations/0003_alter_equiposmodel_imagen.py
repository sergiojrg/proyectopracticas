# Generated by Django 4.0.2 on 2022-02-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_equiposmodel_caducidad_equiposmodel_duracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equiposmodel',
            name='imagen',
            field=models.ImageField(upload_to='EquiposIMG', verbose_name='Imagen'),
        ),
    ]