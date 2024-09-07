from django.contrib import admin
from .models import Categoria, Subcategoria, Producto

# Registrar los modelos en el admin
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
