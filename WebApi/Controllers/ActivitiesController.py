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
from Application.Schemas.ActivitySchema import (
    ActivityRequest,
    ActivityResponse,
    ActivityBaseResponse,
)
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository
from Infrastructure.utils.verifyApiKey import verify_api_key


router = APIRouter()


@router.get("/activities/GetActivities", dependencies=[Depends(verify_api_key)])
async def get_activities():
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivitiesUseCase(activitiesRepository)
    activities = await use_case.execute()
    data = [ActivityResponse.model_validate(activity) for activity in activities]
    return {"message": "success", "data": data, "status": 200}


@router.post(
    "/activities/CreateActivity",
    response_model=ActivityBaseResponse,
    dependencies=[Depends(verify_api_key)],
)
async def create_activity(activity: ActivityRequest):
    activity_model = Activities(**activity.model_dump())
    activityRepository = ActivitiesRepository()
    use_case = CreateActivityUseCase(activityRepository)
    created_activity = await use_case.execute(activity_model)
    return created_activity


@router.put(
    "/activities/UpdateActivity/{activity_id}", dependencies=[Depends(verify_api_key)]
)
async def update_activity(activity_id: int, activity: ActivityRequest):
    activitiesRepository = ActivitiesRepository()
    activity_model = Activities(**activity.model_dump())
    use_case = UpdateActivityUseCase(activitiesRepository)
    update = await use_case.execute(activity_id, activity_model)

    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="actividad para actualizar no existe",
        )

    elif update is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="esta actividad no se puede actualizar debido a que su vigencia está cerrada",
        )

    return {"message": "actividad actualizada correctamente"}


@router.delete(
    "/activities/DeleteActivity/{activity_id}", dependencies=[Depends(verify_api_key)]
)
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
    "/activities/GetActivityById/{activity_id}", dependencies=[Depends(verify_api_key)]
)
async def get_activity_by_id(activity_id: int):
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivityByIdUseCase(activitiesRepository)
    activity = await use_case.execute(activity_id)

    if activity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Esta actividad no existe"
        )

    data = ActivityResponse.model_validate(activity)
    return {"message": "success", "data": data, "status": 200}


@router.get(
    "/activities/GetActivityByName/{activity_name}",
    dependencies=[Depends(verify_api_key)],
)
async def get_activity_by_name(activity_name: str):
    activitiesRepository = ActivitiesRepository()
    use_case = GetActivityByNameUseCase(activitiesRepository)
    activity = await use_case.execute(activity_name.lower().strip())

    if activity is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="esta actividad no existe"
        )

    data = ActivityResponse.model_validate(activity)
    return {"message": "success", "data": data, "status": 200}
