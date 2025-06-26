from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form, status
from fastapi.responses import StreamingResponse
from Application.Schemas.EvidenceSchema import EvidenceSchemaResponse, UpdateEvidence
from Application.UseCases.EvidencesUseCases.CreateEvidenceUseCase import (
    CreateEvidenceUseCase,
)
from Application.UseCases.EvidencesUseCases.UpdateEvidenceUseCase import (
    UpdateEvidenceUseCase,
)
from Application.UseCases.EvidencesUseCases.DeleteEvidenceUseCase import (
    DeleteEvidencesUseCase,
)
from Domain.Entities.Evidences import Evidences
from Infrastructure.Repositories.EvidencesRepository import EvidencesRepository
from Infrastructure.utils.evidence import *
from io import BytesIO
from datetime import date

from Infrastructure.utils.verifyApiKey import verify_api_key

router = APIRouter()


@router.post(
    "/evidence/upload/{actividad_id}",
    dependencies=[Depends(verify_api_key)],
    response_model=List[EvidenceSchemaResponse],
)
async def upload_files(
    actividad_id: int,
    avances: float = Form(...),
    created_at: date = Form(...),
    files: List[UploadFile] = File(...),
):
    repository = EvidencesRepository()
    use_case = CreateEvidenceUseCase(repository)
    evidences_created = []

    for file in files:
        try:
            # Subir archivo a S3
            url, filename = upload_file_to_s3(file, actividad_id)

            # Crear y guardar evidencia
            evidence = Evidences(
                nombre_archivo=filename,
                url_archivo=url,
                actividad_id=actividad_id,
                avances=avances,
                created_at=created_at,
            )
            created = await use_case.execute(evidence)
            evidences_created.append(created)

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error con archivo '{file.filename}': {str(e)}"
            )

    return evidences_created


@router.get(
    "/evidence/download/{actividad_id}/{filename}",
    dependencies=[Depends(verify_api_key)],
)
async def download_file(actividad_id: int, filename: str):
    try:
        file_bytes = download_file_from_s3(actividad_id, filename)
        return StreamingResponse(
            BytesIO(file_bytes),
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/evidence/update/{evidence_id}", dependencies=[Depends(verify_api_key)])
async def update_evidence(evidence_id: int, evidence: UpdateEvidence):
    evidencesRepository = EvidencesRepository()
    use_case = UpdateEvidenceUseCase(evidencesRepository)

    update_evidence = await use_case.execute(
        evidence_id, evidence.created_at, evidence.avances
    )

    if update_evidence is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta evidencia a actualizar no existe",
        )

    return {"message": "evidencia actualizada correctamente"}


@router.delete("/evidence/delete/{evidence_id}", dependencies=[Depends(verify_api_key)])
async def delete_evidence(evidence_id: int):
    evidencesRepository = EvidencesRepository()
    use_case = DeleteEvidencesUseCase(evidencesRepository)

    success = await use_case.execute(evidence_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta evidencia a eliminar no existe",
        )

    return {"message": "evidencia eliminada correctamente"}
