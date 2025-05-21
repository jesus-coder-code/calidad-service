FROM python:alpine

# Establece el directorio de trabajo
WORKDIR /app/calidad-service

# Instala dependencias del sistema necesarias para compilar paquetes de Python
RUN apk add --no-cache gcc musl-dev libffi-dev 

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install "uvicorn[standard]"

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto por defecto de FastAPI (uvicorn)
EXPOSE 8000

# Comando por defecto para ejecutar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]