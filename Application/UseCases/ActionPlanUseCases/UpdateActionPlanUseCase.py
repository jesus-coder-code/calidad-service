from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.Repositories.ActionPlanRepository import ActionPlanRepository


class UpdateActionPlanUseCase:
    def __init__(self):
        self.repository = ActionPlanRepository()

    async def execute(
        self, plan_id: int, updated_plan: ActionPlan
    ) -> ActionPlan | None:
        return await self.repository.updatePlan(plan_id, updated_plan)
