FROM python:3.9.2-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "src/docker-app.py"]
