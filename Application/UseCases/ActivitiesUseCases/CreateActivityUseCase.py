from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository


class CreateActivityUseCase:
    def __init__(self):
        self.repository = ActivitiesRepository()

    async def execute(self, activity: Activities) -> Activities:
        return await self.repository.createActivity(activity)
