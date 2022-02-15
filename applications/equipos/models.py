from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

class EquiposModel(models.Model):
    nombre = models.CharField('Nombre del Equipo',max_length=80)
    marca = models.CharField('Marca',max_length=80)
    telefono = PhoneNumberField(unique = True, null = False, blank = False)
    ingeniero = models.CharField('Nombre del Ingeniero',max_length=120)
    serie = models.CharField('Número de Serie',max_length=80)
    imagen = models.ImageField('Imagen',upload_to='EquiposIMG',blank=False,null=False)  
    imagen2 = models.ImageField('Imagen',null=True,blank=True)
    duracion = models.CharField('Duración de la Póliza',max_length=100, blank=True)
    caducidad = models.CharField('Fecha de caducidad de la Póliza',max_length=100,blank=True)
    terminos = models.TextField()
    incluye = RichTextUploadingField(default=" ",null=True,blank=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.nombre + ' ' + self.marca 