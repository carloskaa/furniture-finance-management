from django.shortcuts import render, redirect
from .models import Income
from django.contrib.auth.decorators import login_required

@login_required
def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'incomes/income_list.html', {'incomes': incomes})

@login_required
def add_income(request):
    tipos_ingreso = Income.TYPE_CHOICES
    if request.method == 'POST':
        date = request.POST['date']
        amount = request.POST['amount']
        description = request.POST['description']
        tipo = request.POST['tipo']  # Asegúrate de que este campo exista en tu plantilla HTML
        Income.objects.create(user=request.user, date=date, amount=amount, description=description, tipo=tipo)
        return redirect('income_list')
    return render(request, 'incomes/add_income.html',{'tipos_ingreso': tipos_ingreso})
    
    