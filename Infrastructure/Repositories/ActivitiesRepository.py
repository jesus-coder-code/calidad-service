from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from Domain.Entities.Activities import Activities
from typing import List
from Infrastructure.DB.Database import get_session


class ActivitiesRepository:
    async def getAllActivities(self) -> List[Activities]:
        async with get_session() as session:
            statement = select(Activities)
            result = await session.execute(statement)
            return result.scalars().all()

    async def createActivity(self, activities: Activities) -> Activities:
        async with get_session() as session:
            session.add(activities)
            await session.commit()
