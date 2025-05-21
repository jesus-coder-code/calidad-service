from Domain.Entities.Activities import Activities
from Infrastructure.Repositories.ActivitiesRepository import ActivitiesRepository
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class CreateActivityUseCase:
    def __init__(self, activitiesRepository: IActivitiesRepository):
        self.repository = activitiesRepository

    async def execute(self, activity: Activities) -> Activities:
        return await self.repository.createActivity(activity)
