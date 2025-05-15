from typing import Optional
from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class UpdateActivityUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(
        self, activity_id: int, updated_activity: Activities
    ) -> Activities | None | bool:
        return await self.repository.updateActivity(activity_id, updated_activity)
