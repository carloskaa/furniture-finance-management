# Generated by Django 5.0.6 on 2024-06-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='tipo',
            field=models.CharField(choices=[('COMIDA', 'Comida'), ('TRANSPORTE', 'Transporte'), ('SALUD', 'Salud')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
