from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository


class DeleteActivityUseCase:
    def __init__(self):
        self.repository = ActivitiesRepository()

    async def execute(self, activity_id: int) -> bool:
        return await self.repository.deleteActivity(activity_id)
