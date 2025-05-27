import os
import boto3
import hmac
import hashlib
import base64
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
CLIENT_SECRET = os.getenv("COGNITO_CLIENT_SECRET")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")


def get_secret_hash(username: str) -> str:
    message = username + CLIENT_ID
    dig = hmac.new(
        CLIENT_SECRET.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    return base64.b64encode(dig).decode()


def authenticate_user(username: str, password: str) -> dict:
    client = boto3.client("cognito-idp", region_name=AWS_REGION)

    try:
        response = client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
                "SECRET_HASH": get_secret_hash(username),
            },
            ClientId=CLIENT_ID,
        )
        return response["AuthenticationResult"]
    except client.exceptions.NotAuthorizedException:
        raise ValueError("Credenciales incorrectas.")
    except client.exceptions.UserNotFoundException:
        raise ValueError("Usuario no encontrado.")
    except Exception as e:
        raise ValueError(f"Error en autenticación: {str(e)}")


def register_user(username: str, name: str, password: str) -> dict:
    client = boto3.client("cognito-idp", region_name=AWS_REGION)

    try:
        response = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password,
            UserAttributes=[
                {"Name": "email", "Value": username},
                {"Name": "name", "Value": name},
            ],
        )
        return response
    except client.exceptions.UsernameExistsException:
        raise ValueError("El usuario ya existe.")
    except Exception as e:
        raise ValueError(f"Error en el registro: {str(e)}")


def confirm_user(username: str, confirmation_code: str) -> dict:
    client = boto3.client("cognito-idp", region_name=AWS_REGION)

    try:
        response = client.confirm_sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            ConfirmationCode=confirmation_code,
        )
        return response
    except client.exceptions.CodeMismatchException:
        raise ValueError("El código de confirmación es incorrecto.")
    except client.exceptions.ExpiredCodeException:
        raise ValueError("El código de confirmación ha expirado.")
    except client.exceptions.UserNotFoundException:
        raise ValueError("Usuario no encontrado.")
    except Exception as e:
        raise ValueError(f"Error al confirmar usuario: {str(e)}")
