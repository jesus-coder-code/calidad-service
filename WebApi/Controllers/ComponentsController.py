from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status

from Application.Schemas.ComponentSchema import ComponentResponse, ComponentSchema
from Application.UseCases.ComponentsUseCases.CreateComponentUseCase import (
    CreateComponentUseCase,
)
from Application.UseCases.ComponentsUseCases.GetComponentsUseCase import (
    GetComponentsUseCase,
)
from Domain.Entities.Components import Components


router = APIRouter()


@router.get("/components/GetComponents", response_model=Dict[str, Any])
async def get_action_plan():
    use_case = GetComponentsUseCase()
    components = await use_case.execute()
    data = [ComponentResponse.model_validate(component) for component in components]
    return {"message": "success", "data": data, "status": 200}


@router.post("/components/CreateComponent")
async def create_component(component: Components):
    use_case = CreateComponentUseCase()
    created_component = await use_case.execute(component)
    return created_component
