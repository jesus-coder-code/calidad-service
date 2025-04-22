from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from Application.UseCases.ActionPlanUseCases.UpdateActionPlanUseCase import (
    UpdateActionPlanUseCase,
)
from Application.UseCases.ActionPlanUseCases.GetActionPlanUseCase import (
    GetActionPlanUseCase,
)
from Application.UseCases.ActionPlanUseCases.CreateActionPlanUseCase import (
    CreateActionPlanUseCase,
)
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository
from Infrastructure.utils.dependencies import verify_api_key
from Application.Schemas.ActionPlanSchema import (
    ActionPlanResponse,
    ActionPlanSchema,
    ActionPlanSchemaResponse,
)

router = APIRouter()


@router.get(
    "/actionplan/GetActionPlan",
    response_model=Dict[str, Any],
)
async def get_action_plan():
    actionPlanRepository = ActionPlanRepository()
    use_case = GetActionPlanUseCase(actionPlanRepository)
    plans = await use_case.execute()
    data = [ActionPlanResponse.model_validate(plan) for plan in plans]
    return {"message": "success", "data": data, "status": 200}


@router.post("/actionplan/CreateActionPlan", response_model=ActionPlanSchemaResponse)
async def create_plan(plan: ActionPlanSchema):
    plan_model = ActionPlan(**plan.model_dump())
    actionPlanRepository = ActionPlanRepository()
    use_case = CreateActionPlanUseCase(actionPlanRepository)
    created_plan = await use_case.execute(plan_model)
    return created_plan


@router.put("/actionplan/UpdateActionPlan/{plan_id}")
async def update_plan(plan_id: int, activity: ActionPlanSchema):
    plan_model = ActionPlan(**activity.model_dump())
    actionPlanRepository = ActionPlanRepository()
    use_case = UpdateActionPlanUseCase(actionPlanRepository)
    update_plan = await use_case.execute(plan_id, plan_model)

    if update_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este plan para actualizar no existe",
        )

    return {"message": "plan de acción actualizado correctamente"}
