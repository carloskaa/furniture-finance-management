# urls.py
from django.urls import path
from .views import CatalogoView
from . import views

urlpatterns = [
    path('new_catalogo/<str:categoria_id>', views.new_catalogo_view, name='new_catalogo'),
    path('new_home/', views.new_home_view, name='new_home'),
    #path('categoria/<str:categoria>/', views.ver_categoria, name='ver_categoria'),
]
