from typing import Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from Application.UseCases.ActivitiesUseCases.DeleteActivityUseCase import (
    DeleteActivityUseCase,
)
from Application.UseCases.ActivitiesUseCases.GetActivitiesUseCase import (
    GetActivitiesUseCase,
)
from Application.UseCases.ActivitiesUseCases.CreateActivityUseCase import (
    CreateActivityUseCase,
)
from Application.UseCases.ActivitiesUseCases.UpdateActivityUseCase import (
    UpdateActivityUseCase,
)
from Domain.Entities.Activities import Activities
from Infrastructure.utils.dependencies import verify_api_key
from Application.Schemas.ActivitySchema import ActivitySchema, ActivitySchemaResponse

router = APIRouter()


@router.get(
    "/activities/GetActivities",
    response_model=Dict[str, Any],
)
async def get_activities():
    use_case = GetActivitiesUseCase()
    activities = await use_case.execute()
    return {"message": "success", "data": activities, "status": 200}


@router.post("/activities/CreateActivity", response_model=ActivitySchemaResponse)
async def create_activity(activity: ActivitySchema):
    activity_model = Activities(**activity.model_dump())
    use_case = CreateActivityUseCase()
    created_activity = await use_case.execute(activity_model)
    return created_activity


@router.put("/activities/UpdateActivity/{activity_id}")
async def update_activity(activity_id: int, activity: ActivitySchema):
    activity_model = Activities(**activity.model_dump())
    use_case = UpdateActivityUseCase()
    update = await use_case.execute(activity_id, activity_model)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="actividad para actualizar no existe",
        )
    return {"message": "actividad actualizada correctamente"}


@router.delete("/activities/DeleteActivity/{activity_id}")
async def delete_activity(activity_id: int):
    use_case = DeleteActivityUseCase()
    success = await use_case.execute(activity_id)

    if success is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Actividad no encontrada"
        )

    return {"message": "Actividad eliminada correctamente"}
