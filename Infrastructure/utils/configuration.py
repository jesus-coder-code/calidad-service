from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


# definir las variables de entorno
class Settings(BaseSettings):
    COGNITO_TOKEN_URL: str
    COGNITO_CLIENT_SECRET: str
    COGNITO_CLIENT_ID: str
    API_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
