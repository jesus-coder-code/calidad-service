from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository


class UpdateActivityUseCase:
    def __init__(self):
        self.repository = ActivitiesRepository()

    async def execute(
        self, activity_id: int, updated_activity: Activities
    ) -> Activities:
        await self.repository.updateActivity(activity_id, updated_activity)
