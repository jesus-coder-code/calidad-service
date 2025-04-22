from typing import List
from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class GetActivitiesUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(self) -> List[Activities]:
        return await self.repository.getAllActivities()
