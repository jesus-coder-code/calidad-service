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
from Application.UseCases.ActivitiesUseCases.GetActivityByNameUseCase import (
    GetActivityByNameUseCase,
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
    "/activities/GetActivityById/{activity_id}",
)
async def get_activity_by_id(activity_id: int):
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivityByIdUseCase(activitiesRepository)
    activity = await use_case.execute(activity_id)

    if activity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Esta actividad no existe"
        )

    data = ActivitySchemaResponse.model_validate(activity)
    return {"message": "success", "data": data, "status": 200}


@router.get("/activities/GetActivityByName/{activity_name}")
async def get_activity_by_name(activity_name: str):
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivityByNameUseCase(activitiesRepository)
    activity = await use_case.execute(activity_name)

    if activity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta actividad no existe"
        )

    data = ActivitySchemaResponse.model_validate(activity)
    return {"message": "success", "data": data, "status": 200}
