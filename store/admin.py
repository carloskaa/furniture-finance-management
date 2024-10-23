from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, Mueble

# Registrar los modelos en el admin
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Mueble)
