from fastapi import APIRouter, Depends, HTTPException, status
from Infrastructure.Repositories.ResponsibleRepository import ResponsibleRepository
from pydantic import EmailStr, ValidationError
from Application.UseCases.ResponsibleUseCases.GetResponsibleUseCase import (
    GetResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCases.GetResponsibleByIdUseCase import (
    GetResponsibleByIdUseCase,
)
from Application.UseCases.ResponsibleUseCases.GetResponsibleByNameUseCase import (
    GetResponsibleByNameUseCase,
)
from Application.UseCases.ResponsibleUseCases.GetResponsibleByEmailUseCase import (
    GetResponsibleByEmailUseCase,
)
from Application.UseCases.ResponsibleUseCases.CreateResponsibleUseCase import (
    CreateResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCases.UpdateResponsibleUseCase import (
    UpdateResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCases.DeleteResponsibleUseCase import (
    DeleteResponsibleUseCase,
)
from Application.Schemas.ResponsibleSchema import (
    ResponsibleSchemaRequest,
    ResponsibleSchemaResponse,
    ResponsibleWithPolitic,
)
from Domain.Entities.Responsible import Responsible
from Infrastructure.utils.verifyApiKey import verify_api_key


router = APIRouter()


@router.get("/responsible/GetResponsible", dependencies=[Depends(verify_api_key)])
async def get_responsible():
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleUseCase(responsibleRepository)
    responsible = await use_case.execute()
    data = [ResponsibleWithPolitic.model_validate(x) for x in responsible]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/responsible/CreateResponsible",
    dependencies=[Depends(verify_api_key)],
    response_model=ResponsibleSchemaResponse,
)
async def create_responsible(responsible: ResponsibleSchemaRequest):
    responsibleRepository = ResponsibleRepository()
    responsible_model = Responsible(**responsible.model_dump())
    use_case = CreateResponsibleUseCase(responsibleRepository)
    created_responsible = await use_case.execute(responsible_model)

    if created_responsible is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ya existe un usuario registrado con este correo",
        )
    return created_responsible


@router.put(
    "/responsible/UpdateResponsible/{responsible_id}",
    dependencies=[Depends(verify_api_key)],
)
async def update_responsible(
    responsible_id: int, responsible: ResponsibleSchemaRequest
):
    responsibleRepository = ResponsibleRepository()
    responsible_model = Responsible(**responsible.model_dump())
    use_case = UpdateResponsibleUseCase(responsibleRepository)
    update = await use_case.execute(responsible_id, responsible_model)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta persona no está registrada",
        )

    return {"message": "datos actualizados correctamente"}


@router.delete(
    "/responsible/DeleteResponsible/{responsible_id}",
    dependencies=[Depends(verify_api_key)],
)
async def delete_responsible(responsible_id: int):
    responsibleRepository = ResponsibleRepository()
    use_case = DeleteResponsibleUseCase(responsibleRepository)
    sucess = await use_case.execute(responsible_id)

    if sucess is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="esta persona no está registrada",
        )

    return {"message": "datos eliminados correctamente"}


@router.get(
    "/responsible/GetResponsibleById/{responsible_id}",
    dependencies=[Depends(verify_api_key)],
)
async def get_responsible_by_id(responsible_id: int):
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleByIdUseCase(responsibleRepository)
    responsible = await use_case.execute(responsible_id)

    if responsible is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no hay datos que coincidan con la búsqueda",
        )

    data = ResponsibleWithPolitic.model_validate(responsible)
    return {"message": "sucess", "data": data, "status": 200}


@router.get(
    "/responsible/GetResponsibleByName/{responsible_name}",
    dependencies=[Depends(verify_api_key)],
)
async def get_responsible_by_name(responsible_name: str):
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleByNameUseCase(responsibleRepository)
    responsible = await use_case.execute(responsible_name.lower().strip())

    if responsible is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no hay datos que coincidan con la búsqueda",
        )

    data = ResponsibleWithPolitic.model_validate(responsible)
    return {"message": "sucess", "data": data, "status": 200}


@router.get(
    "/responsible/GetResponsibleByEmail/{responsible_email}",
    dependencies=[Depends(verify_api_key)],
)
async def get_responsible_by_email(responsible_email: EmailStr):
    use_case = GetResponsibleByEmailUseCase(ResponsibleRepository())
    responsible = await use_case.execute(responsible_email.lower().strip())

    if responsible is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este correo no coincide con ningun responsable",
        )

    data = ResponsibleWithPolitic.model_validate(responsible)
    return {"message": "success", "data": data, "status": 200}
