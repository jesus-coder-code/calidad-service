from Domain.Entities.Activities import Activities
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class GetActivityByIdUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(self, activity_id: int) -> Activities | None:
        return await self.repository.getActivityById(activity_id)
