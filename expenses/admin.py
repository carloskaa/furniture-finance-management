from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'description', 'tipo', 'user']
    list_editable = ['tipo']

admin.site.register(Expense, ExpenseAdmin) ###hacer editable la base de datos desde django admin
