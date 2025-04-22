from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class DeleteActivityUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(self, activity_id: int) -> bool:
        return await self.repository.deleteActivity(activity_id)
