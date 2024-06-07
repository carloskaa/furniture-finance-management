from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    tipos_gasto = Expense.TYPE_CHOICES
    if request.method == 'POST':
        date = request.POST['date']
        amount = request.POST['amount']
        description = request.POST['description']
        tipo = request.POST['tipo']  # Asegúrate de que este campo exista en tu plantilla HTML
        Expense.objects.create(user=request.user, date=date, amount=amount, description=description, tipo=tipo)
        return redirect('expense_list')
    return render(request, 'expenses/add_expense.html',{'tipos_gasto': tipos_gasto})

