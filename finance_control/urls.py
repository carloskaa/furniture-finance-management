from django.urls import path
from . import views
app_name = 'finance_control'

urlpatterns = [
    path('inicio', views.home, name='home'),
    path('agregar-gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('agregar-ingreso/', views.agregar_ingreso, name='agregar_ingreso'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
