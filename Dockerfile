# Usa una imagen base oficial de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y luego instálalos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Instala Node.js y npm
RUN apt-get update && \
    apt-get install -y nodejs npm

# Copia el archivo package.json y package-lock.json (si existe) y luego instala las dependencias de npm
COPY theme/static_src/package*.json /app/theme/static_src/
WORKDIR /app/theme/static_src/
RUN npm install
RUN npm run build:css

# Copia el resto del código de la aplicación
WORKDIR /app
COPY . /app/

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el servidor de producción Gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

