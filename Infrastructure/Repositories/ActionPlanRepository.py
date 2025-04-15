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
