from typing import List
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository
from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class GetActionPlanUseCase:
    def __init__(self, actionPlanrepository: IActionPlanRepository):
        self.repository = actionPlanrepository

    async def execute(self) -> List[ActionPlan]:
        return await self.repository.getAllPlans()
