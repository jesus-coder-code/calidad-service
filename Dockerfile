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

ENV API_KEY=4ZGZgqwlf3yZKvIBoPLxQ4iOmDUS4gTx1MevMkOHMbdsf96f1szpLNkWUDVMqEIe0BIUYlwvivFhgmYxAwOXYvuZ5vzpAxn0nzByXTTYw5yOCyOBL0jhE0w5OOPDRtQJ
ENV COGNITO_CLIENT_ID=780tmft6g8atim94ucebs3skbh
ENV COGNITO_CLIENT_SECRET=1e00tghg3dk6bc1tlu0nebrsoh29utjk9gt96d7k054qs06s3q5n
ENV COGNITO_TOKEN_URL=https://us-east-1otvp4rbq5.auth.us-east-1.amazoncognito.com/oauth2/token
ENV DATABASE_URL=postgresql+asyncpg://jesusalways:51246380@postgresql-jesusalways.alwaysdata.net/jesusalways_calidaddb

# Expone el puerto por defecto de FastAPI (uvicorn)
EXPOSE 8000

# Comando por defecto para ejecutar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]