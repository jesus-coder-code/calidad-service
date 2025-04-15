from pydantic_settings import BaseSettings


# definir las variables de entorno
class Settings(BaseSettings):
    COGNITO_ENDPOINT: str
    COGNITO_CLIENT_SECRET: str
    COGNITO_CLIENT_ID: str
    API_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
