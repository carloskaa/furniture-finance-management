# urls.py
from django.urls import path
from .views import CatalogoView

urlpatterns = [
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
]
