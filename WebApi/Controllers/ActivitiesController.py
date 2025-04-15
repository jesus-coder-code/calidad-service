from typing import Any, Dict
from fastapi import APIRouter, Depends
from Application.UseCases.ActivitiesUseCases.GetActivitiesUseCase import (
    GetActivitiesUseCase,
)
from Application.UseCases.ActivitiesUseCases.CreateActivityUseCase import (
    CreateActivityUseCase,
)
from Domain.Entities.Activities import Activities
from Infrastructure.utils.dependencies import verify_api_key
from Application.Schemas.ActivitySchema import ActivitySchema

router = APIRouter()


@router.get(
    "/activities/GetActivities",
    response_model=Dict[str, Any],
)
async def get_activities():
    use_case = GetActivitiesUseCase()
    activities = await use_case.execute()
    return {"message": "success", "data": activities, "status": 200}


@router.post("/activities/CreateActivity")
async def create_activity(activity: ActivitySchema):
    activity_model = Activities(**activity.model_dump())
    use_case = CreateActivityUseCase()
    await use_case.execute(activity_model)
    return {"message": "actividad registrada correctamente"}
