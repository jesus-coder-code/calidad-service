from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository


class CreateActionPlanUseCase:
    def __init__(self):
        self.repository = ActionPlanRepository()

    async def execute(self, plans: ActionPlan) -> ActionPlan:
        return await self.repository.createPlan(plans)
