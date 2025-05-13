import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
COGNITO_TOKEN_URL = os.environ["COGNITO_TOKEN_URL"]
COGNITO_CLIENT_SECRET = os.environ["COGNITO_CLIENT_SECRET"]
COGNITO_CLIENT_ID = os.environ["COGNITO_CLIENT_ID"]
API_KEY = os.environ["API_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
