from typing import List
from sqlmodel import select
from sqlalchemy.orm import selectinload
from Domain.Entities.ActionPlan import ActionPlan
from Infrastructure.DB.Database import get_session


class ActionPlanRepository:
    async def getAllPlans(self) -> List[ActionPlan]:
        async with get_session() as session:
            statement = select(ActionPlan).options(selectinload(ActionPlan.actividades))
            result = await session.execute(statement)
            return result.scalars().all()

    async def createPlan(self, plans: ActionPlan) -> ActionPlan:
        async with get_session() as session:
            session.add(plans)
            await session.commit()

    async def updatePlan(self, plan_id: int, plans: ActionPlan) -> ActionPlan:
        async with get_session() as session:
            plan_exists = await session.execute(
                select(ActionPlan).where(ActionPlan.id == plan_id)
            )
            existing_plan = plan_exists.scalars().first()

            if not existing_plan:
                raise ValueError("Este plan de acción no existe")

            for key, value in plans.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(existing_plan, key)
                ):
                    setattr(existing_plan, key, value)

            await session.commit()
            return existing_plan
