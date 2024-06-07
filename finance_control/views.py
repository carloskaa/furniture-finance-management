from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from expenses.models import Expense
from incomes.models import Income
from django.db.models import Sum

@login_required
def home(request):
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_incomes = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'home.html', {'total_expenses': total_expenses, 'total_incomes': total_incomes})


def logout_sesion(request):
    logout(request)
    return redirect('login')  # Asumiendo que tienes una URL llamada 'login'