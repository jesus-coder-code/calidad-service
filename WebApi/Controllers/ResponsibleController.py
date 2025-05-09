from fastapi import APIRouter, HTTPException, status
from Infrastructure.Repositories.ResponsibleRepository import ResponsibleRepository
from Application.UseCases.ResponsibleUseCase.GetResponsibleUseCase import (
    GetResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCase.GetResponsibleByIdUseCase import (
    GetResponsibleByIdUseCase,
)
from Application.UseCases.ResponsibleUseCase.GetResponsibleByNameUseCase import (
    GetResponsibleByNameUseCase,
)
from Application.UseCases.ResponsibleUseCase.CreateResponsibleUseCase import (
    CreateResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCase.UpdateResponsibleUseCase import (
    UpdateResponsibleUseCase,
)
from Application.UseCases.ResponsibleUseCase.DeleteResponsibleUseCase import (
    DeleteResponsibleUseCase,
)
from Application.Schemas.ResponsibleSchema import (
    ResponsibleSchemaRequest,
    ResponsibleSchemaResponse,
)
from Domain.Entities.Responsible import Responsible


router = APIRouter()


@router.get("/responsible/GetResponsible")
async def get_responsible():
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleUseCase(responsibleRepository)
    responsible = await use_case.execute()
    data = [ResponsibleSchemaResponse.model_validate(x) for x in responsible]
    return {"message": "success", "data": data, "status": 200}


@router.post("/responsible/CreateResponsible", response_model=ResponsibleSchemaResponse)
async def create_responsible(responsible: ResponsibleSchemaRequest):
    responsibleRepository = ResponsibleRepository()
    responsible_model = Responsible(**responsible.model_dump())
    use_case = CreateResponsibleUseCase(responsibleRepository)
    created_responsible = await use_case.execute(responsible_model)
    return created_responsible


@router.put("/responsible/UpdateResponsible/{responsible_id}")
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


@router.delete("/responsible/DeleteResponsible/{responsible_id}")
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


@router.get("/responsible/GetResponsibleById/{responsible_id}")
async def get_responsible_by_id(responsible_id: int):
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleByIdUseCase(responsibleRepository)
    responsible = await use_case.execute(responsible_id)

    if responsible is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no hay datos que coincidan con la búsqueda",
        )

    data = ResponsibleSchemaResponse.model_validate(responsible)
    return {"message": "sucess", "data": data, "status": 200}


@router.get("/responsible/GetResponsibleByName/{responsible_name}")
async def get_responsible_by_name(responsible_name: str):
    responsibleRepository = ResponsibleRepository()
    use_case = GetResponsibleByNameUseCase(responsibleRepository)
    responsible = await use_case.execute(responsible_name.lower().strip())

    if responsible is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no hay datos que coincidan con la búsqueda",
        )

    data = ResponsibleSchemaResponse.model_validate(responsible)
    return {"message": "sucess", "data": data, "status": 200}
