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
from Application.UseCases.ActivitiesUseCases.GetActivityByIdUseCase import (
    GetActivityByIdUseCase,
)
from Application.UseCases.ActivitiesUseCases.UpdateActivityUseCase import (
    UpdateActivityUseCase,
)
from Domain.Entities.Activities import Activities
from Infrastructure.utils.dependencies import verify_api_key
from Application.Schemas.ActivitySchema import ActivitySchema, ActivitySchemaResponse
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository


router = APIRouter()


@router.get(
    "/activities/GetActivities",
    response_model=Dict[str, Any],
)
async def get_activities():
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivitiesUseCase(activitiesRepository)
    activities = await use_case.execute()
    return {"message": "success", "data": activities, "status": 200}


@router.post("/activities/CreateActivity", response_model=ActivitySchemaResponse)
async def create_activity(activity: ActivitySchema):
    activitiesRepository = ActivitiesRepository()
    activity_model = Activities(**activity.model_dump())
    use_case = CreateActivityUseCase(activitiesRepository)
    created_activity = await use_case.execute(activity_model)
    return created_activity


@router.put("/activities/UpdateActivity/{activity_id}")
async def update_activity(activity_id: int, activity: ActivitySchema):
    activitiesRepository = ActivitiesRepository()
    activity_model = Activities(**activity.model_dump())
    use_case = UpdateActivityUseCase(activitiesRepository)
    update = await use_case.execute(activity_id, activity_model)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="actividad para actualizar no existe",
        )
    return {"message": "actividad actualizada correctamente"}


@router.delete("/activities/DeleteActivity/{activity_id}")
async def delete_activity(activity_id: int):
    activitiesRepository = ActivitiesRepository()
    use_case = DeleteActivityUseCase(activitiesRepository)
    success = await use_case.execute(activity_id)

    if success is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Actividad no encontrada"
        )

    return {"message": "Actividad eliminada correctamente"}


@router.get(
    "/activities/GetActivityById",
    response_model=Dict[str, Any],
)
async def get_activities(activity_id: int):
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivityByIdUseCase(activitiesRepository)
    activity = await use_case.execute(activity_id)

    if activity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Esta actividad no existe"
        )

    return {"message": "success", "data": activity, "status": 200}
