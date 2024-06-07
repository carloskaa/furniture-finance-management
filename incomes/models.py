from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    TYPE_CHOICES = [
        ('SALARIO', 'Salario'),
        ('NEGOCIO', 'Negocio'),
        ('INVERSION', 'Inversión'),
        # Agrega más tipos según sea necesario
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    tipo = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"Ingreso - {self.date} - {self.amount} - {self.description} - {self.tipo}"
