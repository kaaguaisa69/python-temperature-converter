# Usar la imagen oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Exponer el puerto 80 para acceder a la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
