from typing import List
from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository


class GetActivitiesUseCase:
    def __init__(self):
        self.repository = ActivitiesRepository()

    async def execute(self) -> List[Activities]:
        return await self.repository.getAllActivities()
