from django.contrib import admin
from .models import EquiposModel

class EquiposAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','marca')
    search_fields = ('nombre','marca','caducidad')
    list_filter = ('nombre','marca','caducidad')

admin.site.register(EquiposModel,EquiposAdmin)