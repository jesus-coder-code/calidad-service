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

    async def updateActivity(
        self, activity_id: int, activities: Activities
    ) -> Activities:
        async with get_session() as session:
            activity_found = await session.execute(
                select(Activities).where(Activities.id == activity_id)
            )
            exists_activity = activity_found.scalars().first()

            if not exists_activity:
                # raise ValueError("esta actividad no existe")
                return None

            for key, value in activities.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(exists_activity, key)
                ):
                    setattr(exists_activity, key, value)

            await session.commit()
            return exists_activity

    async def deleteActivity(self, activity_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(Activities).where(Activities.id == activity_id)
            )
            activity = result.scalars().first()

            if not activity:
                return False

            await session.delete(activity)
            await session.commit()
            return True
