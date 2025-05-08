from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from Domain.Entities.Activities import Activities
from typing import List, Optional
from Infrastructure.DB.Database import get_session
from Domain.Interfaces.IActivitiesRepository import IActivitiesRepository


class ActivitiesRepository(IActivitiesRepository):
    async def getAllActivities(self) -> List[Activities]:
        async with get_session() as session:
            statement = select(Activities)
            result = await session.execute(statement)
            return result.scalars().all()

    async def createActivity(self, activities: Activities) -> Activities:
        async with get_session() as session:
            session.add(activities)
            await session.commit()
            await session.refresh(activities)
            return activities

    async def updateActivity(
        self, activity_id: int, activities: Activities
    ) -> Activities | None:
        async with get_session() as session:
            activity_found = await session.execute(
                select(Activities).where(Activities.id == activity_id)
            )
            exists_activity = activity_found.scalar_one_or_none()

            if exists_activity is None:
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

            if activity is None:
                return False

            await session.delete(activity)
            await session.commit()
            return True

    async def getActivityById(self, activity_id: int) -> Activities | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Activities).where(Activities.id == activity_id)
            )
            existing_activity = statement.scalar_one_or_none()

            if existing_activity is None:
                return None

            return existing_activity

    async def getActivityByName(self, activity_name: str) -> Activities | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Activities).where(Activities.nombre == activity_name)
            )
            existing_activity = statement.scalar_one_or_none()

            if existing_activity is None:
                return None

            return existing_activity
