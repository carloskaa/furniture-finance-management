from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def agregar_gasto(request):
    return render(request, 'agregar_gasto.html')

@login_required
def agregar_ingreso(request):
    return render(request, 'agregar_ingreso.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Asumiendo que tienes una URL llamada 'login'