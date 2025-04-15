from typing import List
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository


class GetActionPlanUseCase:
    def __init__(self):
        self.repository = ActionPlanRepository()

    async def execute(self) -> List[ActionPlan]:
        return await self.repository.getAllPlans()
