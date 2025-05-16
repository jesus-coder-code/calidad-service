from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from Application.Schemas.EvidenceSchema import EvidenceSchemaResponse
from Application.UseCases.EvidencesUseCases.CreateEvidenceUseCase import (
    CreateEvidenceUseCase,
)
from Domain.Entities.Evidences import Evidences
from Infrastructure.Repositories.EvidencesRepository import EvidencesRepository
from Infrastructure.utils.evidence import *
from io import BytesIO

router = APIRouter()


"""@router.post("/upload/{actividad_id}")
async def upload_file(file: UploadFile = File(...)):
    try:
        url, filename = upload_file_to_s3(file)
        return {
            "message": "Archivo subido exitosamente",
            "url": url,
            "filename": filename,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))"""

repository = EvidencesRepository()
use_case = CreateEvidenceUseCase(repository)


@router.post("/upload/{actividad_id}", response_model=List[EvidenceSchemaResponse])
async def upload_files(
    actividad_id: int,
    files: List[UploadFile] = File(...),
):
    repository = EvidencesRepository()
    use_case = CreateEvidenceUseCase(repository)
    evidences_created = []

    for file in files:
        try:
            # Subir archivo a S3
            url, filename = upload_file_to_s3(file)

            # Crear y guardar evidencia
            evidence = Evidences(
                nombre_archivo=filename, url_archivo=url, actividad_id=actividad_id
            )
            created = await use_case.execute(evidence)
            evidences_created.append(created)

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error con archivo '{file.filename}': {str(e)}"
            )

    return evidences_created


@router.get("/download/{filename}")
async def download_file(filename: str):
    try:
        file_bytes = download_file_from_s3(filename)
        return StreamingResponse(
            BytesIO(file_bytes),
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
