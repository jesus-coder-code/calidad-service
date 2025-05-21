from Domain.Entities.ActionPlan import ActionPlan
from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class GetActionPlanByIdUseCase:
    def __init__(self, actionPlanRepository: IActionPlanRepository):
        self.repository = actionPlanRepository

    async def execute(self, plan_id: int) -> ActionPlan | None:
        return await self.repository.getPlanById(plan_id)
