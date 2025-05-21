from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class DeleteActionPlanUseCase:
    def __init__(self, actionPlanRepository: IActionPlanRepository):
        self.repository = actionPlanRepository

    async def execute(self, plan_id: int) -> bool:
        return await self.repository.deletePlan(plan_id)
