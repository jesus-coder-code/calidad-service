from typing import Any, Dict
from fastapi import APIRouter, Depends
from Application.UseCases.ActionPlanUseCases.GetActionPlanUseCase import (
    GetActionPlanUseCase,
)
from Application.UseCases.ActionPlanUseCases.CreateActionPlanUseCase import (
    CreateActionPlanUseCase,
)
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.utils.dependencies import verify_api_key
from Application.Schemas.ActionPlanSchema import ActionPlanResponse

router = APIRouter()


@router.get(
    "/actionplan/GetActionPlan",
    response_model=Dict[str, Any],
)
async def get_action_plan():
    use_case = GetActionPlanUseCase()
    plans = await use_case.execute()
    data = [ActionPlanResponse.model_validate(plan) for plan in plans]
    return {"message": "success", "data": data, "status": 200}


@router.post("/actionplan/CreateActionPlan")
async def create_plan(plan: ActionPlan):
    use_case = CreateActionPlanUseCase()
    await use_case.execute(plan)
    return {"message": "plan de acción creado correctamente"}
