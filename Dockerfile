# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y netcat gcc libpq-dev \
    && apt-get clean

# Install Tailwind CSS
RUN npm install -g tailwindcss

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Run Tailwind build process
RUN python manage.py tailwind install

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the Django server
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 & python manage.py tailwind start"]
