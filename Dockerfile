# Usa una imagen base oficial de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y luego instálalos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Expone el puerto en el que corre Django
EXPOSE 8000

# Define el comando por defecto
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]