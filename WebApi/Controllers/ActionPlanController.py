from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from Application.UseCases.ActionPlanUseCases.DeleteActionPlanUseCase import (
    DeleteActionPlanUseCase,
)
from Application.UseCases.ActionPlanUseCases.GetActionPlanByIdUseCase import (
    GetActionPlanByIdUseCase,
)
from Application.UseCases.ActionPlanUseCases.GetActionPlanByNameUseCase import (
    GetActionPlanByNameUseCase,
)
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


@router.delete("/actionPlan/DelecteActionPlan/{plan_id}")
async def delete_plan(plan_id: int):
    actionPlanRepository = ActionPlanRepository()
    use_case = DeleteActionPlanUseCase(actionPlanRepository)
    success = await use_case.execute(plan_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="plan de accion no encontrado"
        )

    return {"message": "plan de acción eliminado correctamente"}


@router.get(
    "/actionplan/GetActionPlanById/{plan_id}",
)
async def get_action_plan_by_id(plan_id: int):
    actionPlanRepository = ActionPlanRepository()
    use_case = GetActionPlanByIdUseCase(actionPlanRepository)
    plan = await use_case.execute(plan_id)

    if plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este plan de acción no existe",
        )

    data = ActionPlanResponse.model_validate(plan)
    return {"message": "success", "data": data, "status": 200}


@router.get("/actionPlan/GetActionPlanByName/{plan_name}")
async def get_plan_by_name(plan_name: str):
    actionPlanRepository = ActionPlanRepository()
    use_case = GetActionPlanByNameUseCase(actionPlanRepository)
    plan = await use_case.execute(plan_name)

    if plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="este plan de accion no existe",
        )

    data = ActionPlanResponse.model_validate(plan)
    return {"message": "success", "data": data, "status": 200}
