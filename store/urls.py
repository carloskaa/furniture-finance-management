# urls.py
from django.urls import path
from .views import CatalogoView
from . import views

urlpatterns = [
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
    path('new-home/', views.new_home_view, name='new-home'),
]
