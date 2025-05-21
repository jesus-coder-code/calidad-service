from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from Application.Schemas.SubcomponentSchema import (
    SubcomponentBaseResponse,
    SubcomponentSchema,
    SubcomponentSchemaResponse,
)
from Application.UseCases.SubcomponentsUseCases.GetSubcomponentByIdUseCase import (
    GetSubcomponentByIdUseCase,
)
from Application.UseCases.SubcomponentsUseCases.GetSubcomponentsUseCase import (
    GetSubcomponentsUseCase,
)
from Application.UseCases.SubcomponentsUseCases.CreateSubcomponentUseCase import (
    CreateSubcomponentUseCase,
)
from Application.UseCases.SubcomponentsUseCases.UpdateSubcomponentUseCase import (
    UpdateSubcomponentUseCase,
)
from Application.UseCases.SubcomponentsUseCases.DeleteSubcomponentUseCase import (
    DeleteSubcomponentUseCase,
)
from Domain.Entities.Subcomponents import Subcomponents
from Infrastructure.Repositories.SubcomponentsRepository import SubcomponentsRepository
from Infrastructure.utils.verifyApiKey import verify_api_key

router = APIRouter()


@router.get("/subcomponents/GetSubcomponents", dependencies=[Depends(verify_api_key)])
async def get_subcomponents():
    subcomponentsRepository = SubcomponentsRepository()
    use_case = GetSubcomponentsUseCase(subcomponentsRepository)
    subcomponents = await use_case.execute()
    data = [
        SubcomponentBaseResponse.model_validate(subcomponent)
        for subcomponent in subcomponents
    ]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/subcomponents/CreateSubcomponent",
    dependencies=[Depends(verify_api_key)],
    response_model=SubcomponentSchemaResponse,
)
async def create_subcomponent(subcomponent: SubcomponentSchema):
    subcomponentsRepository = SubcomponentsRepository()
    subcomponent_model = Subcomponents(**subcomponent.model_dump())
    use_case = CreateSubcomponentUseCase(subcomponentsRepository)
    created_subcomponent = await use_case.execute(subcomponent_model)
    return created_subcomponent


@router.put(
    "/subcomponents/UpdateSubcomponent/{subcomponent_id}",
    dependencies=[Depends(verify_api_key)],
)
async def update_subcomponent(subcomponent_id: int, subcomponent: SubcomponentSchema):
    subcomponentsRepository = SubcomponentsRepository()
    subcomponent_model = Subcomponents(**subcomponent.model_dump())
    use_case = UpdateSubcomponentUseCase(subcomponentsRepository)
    update = await use_case.execute(subcomponent_id, subcomponent_model)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="este subcomponente no existe"
        )
    return {"message": "subcomponente actualizado"}


@router.delete(
    "/subcomponents/DeleteSubcomponent/{subcomponent_id}",
    dependencies=[Depends(verify_api_key)],
)
async def delete_subcomponent(subcomponent_id: int):
    subcomponentsRepository = SubcomponentsRepository()
    use_case = DeleteSubcomponentUseCase(subcomponentsRepository)
    success = await use_case.execute(subcomponent_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="este subcomponente no existe"
        )

    return {"message": "Subcomponente eliminado correctamente"}


@router.get(
    "/subcomponents/GetSubcomponentById/{subcomponent_id}",
    dependencies=[Depends(verify_api_key)],
)
async def get_subcomponent_by_id(subcomponent_id: int):
    subcomponentsRepository = SubcomponentsRepository()
    use_case = GetSubcomponentByIdUseCase(subcomponentsRepository)
    subcomponent = await use_case.execute(subcomponent_id)

    if subcomponent is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este subcomponente no existe",
        )

    data = SubcomponentBaseResponse.model_validate(subcomponent)
    return {"message": "success", "data": data, "status": 200}
