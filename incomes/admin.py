from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'description', 'tipo', 'user']
    list_editable = ['tipo']

admin.site.register(Income, IncomeAdmin) ###hacer editable la base de datos desde django admin
