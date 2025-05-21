from Domain.Entities.Activities import Activities
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class GetActivityByNameUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(self, activity_name: str) -> Activities | None:
        return await self.repository.getActivityByName(activity_name)
