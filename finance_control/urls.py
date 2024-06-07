from django.urls import path
from .views import home, logout_sesion

urlpatterns = [
    path('home', home, name='home'),
    path('logout_sesion/', logout_sesion, name='logout_sesion'),
]
