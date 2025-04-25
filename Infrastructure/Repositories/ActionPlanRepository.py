from typing import List
from sqlmodel import select
from sqlalchemy.orm import selectinload
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.DB.Database import get_session
from Domain.Interfaces.IActionPlanRepository import IActionPlanRepository


class ActionPlanRepository(IActionPlanRepository):
    async def getAllPlans(self) -> List[ActionPlan]:
        async with get_session() as session:
            statement = select(ActionPlan).options(selectinload(ActionPlan.actividades))
            result = await session.execute(statement)
            return result.scalars().all()

    async def createPlan(self, plans: ActionPlan) -> ActionPlan | None:
        async with get_session() as session:
            session.add(plans)
            await session.commit()
            await session.refresh(plans)
            return plans

    async def updatePlan(self, plan_id: int, plans: ActionPlan) -> ActionPlan:
        async with get_session() as session:
            plan_exists = await session.execute(
                select(ActionPlan).where(ActionPlan.id == plan_id)
            )
            existing_plan = plan_exists.scalars().first()

            if existing_plan is None:
                return None

            for key, value in plans.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(existing_plan, key)
                ):
                    setattr(existing_plan, key, value)

            await session.commit()
            return existing_plan

    async def deletePlan(self, plan_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(ActionPlan).where(ActionPlan.id == plan_id)
            )
            plan = result.scalars().first()

            if plan is None:
                return False

            await session.delete(plan)
            await session.commit()
            return True
