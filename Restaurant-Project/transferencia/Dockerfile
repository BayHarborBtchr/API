# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios
COPY transferencia.py .
COPY Cleaned_Menu.csv .

# Instala las dependencias necesarias
RUN pip install mysql-connector-python pandas

# Comando por defecto para ejecutar el script
CMD ["python", "transferencia.py"]
