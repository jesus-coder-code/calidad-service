from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository
from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class UpdateActionPlanUseCase:
    def __init__(self, actionPlanRepository: IActionPlanRepository):
        self.repository = actionPlanRepository

    async def execute(
        self, plan_id: int, updated_plan: ActionPlan
    ) -> ActionPlan | None | bool:
        return await self.repository.updatePlan(plan_id, updated_plan)
