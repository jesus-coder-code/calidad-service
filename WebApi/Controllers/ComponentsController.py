from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status

from Application.Schemas.ComponentSchema import (
    ComponentResponse,
    ComponentSchema,
    ComponentSchemaResponse,
)
from Application.UseCases.ComponentsUseCases.CreateComponentUseCase import (
    CreateComponentUseCase,
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
async def get_action_plan():
    componentsRepository = ComponentsRepository()
    use_case = GetComponentsUseCase(componentsRepository)
    components = await use_case.execute()
    data = [ComponentResponse.model_validate(component) for component in components]
    return {"message": "success", "data": data, "status": 200}


@router.post("/components/CreateComponent", response_model=ComponentSchemaResponse)
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
