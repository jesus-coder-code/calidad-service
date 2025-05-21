from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository
from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class CreateActionPlanUseCase:
    def __init__(self, actionPlanRepository: IActionPlanRepository):
        self.repository = actionPlanRepository

    async def execute(self, plans: ActionPlan) -> ActionPlan:
        return await self.repository.createPlan(plans)
