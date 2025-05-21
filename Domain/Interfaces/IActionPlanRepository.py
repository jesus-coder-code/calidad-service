from abc import ABC, abstractmethod
from typing import List
from Domain.Entities.ActionPlan import ActionPlan


class IActionPlanRepository(ABC):
    @abstractmethod
    async def getAllPlans(self) -> List[ActionPlan]:
        pass

    @abstractmethod
    async def createPlan(self, plans: ActionPlan) -> ActionPlan | None:
        pass

    @abstractmethod
    async def updatePlan(
        self, plan_id: int, plans: ActionPlan
    ) -> ActionPlan | None | bool:
        pass

    @abstractmethod
    async def deletePlan(self, plan_id: int) -> bool:
        pass

    @abstractmethod
    async def getPlanById(self, plan_id: int) -> ActionPlan | None:
        pass

    @abstractmethod
    async def getPlanByName(self, plan_name: str) -> ActionPlan | None:
        pass
