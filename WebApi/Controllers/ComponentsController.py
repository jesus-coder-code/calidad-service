from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status

from Application.Schemas.ComponentSchema import (
    ComponentResponse,
    ComponentSchema,
    ComponentSchemaBaseResponse,
)
from Application.UseCases.ComponentsUseCases.CreateComponentUseCase import (
    CreateComponentUseCase,
)
from Application.UseCases.ComponentsUseCases.DeleteComponentUseCase import (
    DeleteComponentUseCase,
)
from Application.UseCases.ComponentsUseCases.GetComponentByIdUseCase import (
    GetComponentByIdUseCase,
)
from Application.UseCases.ComponentsUseCases.GetComponentsUseCase import (
    GetComponentsUseCase,
)
from Application.UseCases.ComponentsUseCases.UpdateComponentsUseCase import (
    UpdateComponentsUseCase,
)
from Domain.Entities.Components import Components
from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository


router = APIRouter()


@router.get("/components/GetComponents", response_model=Dict[str, Any])
async def get_component():
    componentsRepository = ComponentsRepository()
    use_case = GetComponentsUseCase(componentsRepository)
    components = await use_case.execute()
    data = [ComponentResponse.model_validate(component) for component in components]
    return {"message": "success", "data": data, "status": 200}


@router.post("/components/CreateComponent", response_model=ComponentSchemaBaseResponse)
async def create_component(component: ComponentSchema):
    component_model = Components(**component.model_dump())
    componentsRepository = ComponentsRepository()
    use_case = CreateComponentUseCase(componentsRepository)
    created_component = await use_case.execute(component_model)
    return created_component


@router.put("/components/UpdateComponent/{component_id}")
async def update_component(component_id: int, component: ComponentSchema):
    componentsRepository = ComponentsRepository()
    component_model = Components(**component.model_dump())
    use_case = UpdateComponentsUseCase(componentsRepository)
    update_component = await use_case.execute(component_id, component_model)

    if update_component is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este componente para actualizar no existe",
        )

    return {"message": "componente actualizado correctamente"}


@router.delete("/components/DeleteComponent/{component_id}")
async def delete_component(component_id: int):
    componentRepository = ComponentsRepository()
    use_case = DeleteComponentUseCase(componentRepository)
    success = await use_case.execute(component_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="este componente no existe"
        )

    return {"message": "componente eliminado correctamente"}


@router.get("/components/GetComponents/{component_id}", response_model=Dict[str, Any])
async def get_component(component_id: int):
    componentsRepository = ComponentsRepository()
    use_case = GetComponentByIdUseCase(componentsRepository)
    component = await use_case.execute(component_id)

    if component is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="este componente no existe"
        )
    data = ComponentResponse.model_validate(component)

    return {"message": "success", "data": data, "status": 200}
