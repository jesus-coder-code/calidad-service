from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class GetActionPlanByNameUseCase:
    def __init__(self, actionPlanRepository: IActionPlanRepository):
        self.repository = actionPlanRepository

    async def execute(self, plan_name: str):
        return await self.repository.getPlanByName(plan_name)
