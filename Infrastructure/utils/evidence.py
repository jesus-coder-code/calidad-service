import boto3
from botocore.exceptions import BotoCoreError, ClientError
from fastapi import UploadFile
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_REGION = os.getenv("AWS_REGION")
BASE_FOLDER = os.getenv("BASE_FOLDER")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=S3_REGION,
)


def upload_file_to_s3(
    file: UploadFile, actividad_id: int, folder: str = BASE_FOLDER
) -> str:
    # Extraer la extensión original
    _, extension = os.path.splitext(file.filename)

    # Formatear fecha y hora actual
    timestamp = datetime.now().strftime("%d_%m_%Y_%H:%M:%S")

    # Construir nuevo nombre de archivo
    new_filename = f"SEGUIMIENTO_{timestamp}{extension}"

    # Construir la key en S3
    key = f"{folder}/actividad_{actividad_id}/{new_filename}"

    try:
        s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, key)
        url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{key}"
        return url, new_filename
    except (BotoCoreError, ClientError) as e:
        raise Exception(f"Error al subir archivo: {str(e)}")


def download_file_from_s3(
    actividad_id: int, filename: str, folder: str = BASE_FOLDER
) -> bytes:
    # key = os.path.join(folder, filename)
    key = f"{folder.rstrip('/')}/actividad_{actividad_id}/{filename}"
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=key)
        return response["Body"].read()
    except (BotoCoreError, ClientError) as e:
        raise Exception(f"Error al descargar archivo: {str(e)}")
