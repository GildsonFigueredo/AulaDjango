from django.contrib import admin

# Register your models here.
from .models import usuario
@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
   list_display = ('id', 'nome', 'idade')