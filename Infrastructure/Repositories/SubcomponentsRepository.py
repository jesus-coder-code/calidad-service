from sqlmodel import select
from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository
from Domain.Entities.Subcomponents import Subcomponents
from typing import List
from Infrastructure.DB.Database import get_session
from sqlalchemy.orm import selectinload


class SubcomponentsRepository(ISubcomponentsRepository):
    async def getAllSubcomponents(self) -> List[Subcomponents]:
        async with get_session() as session:
            statement = select(Subcomponents).options(
                selectinload(Subcomponents.actividades)
            )
            result = await session.execute(statement)
            return result.scalars().all()

    async def createSubcomponent(self, subcomponents: Subcomponents) -> Subcomponents:
        async with get_session() as session:
            session.add(subcomponents)
            await session.commit()
            await session.refresh(subcomponents)
            return subcomponents

    async def updateSubcomponent(
        self, subcomponent_id: int, subcomponents: Subcomponents
    ) -> Subcomponents | None:
        async with get_session() as session:
            subcomponent_found = await session.execute(
                select(Subcomponents).where(Subcomponents.id == subcomponent_id)
            )
            exists_subcomponent = subcomponent_found.scalar_one_or_none()

            if exists_subcomponent is None:
                return None

            for key, value in subcomponents.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(exists_subcomponent, key)
                ):
                    setattr(exists_subcomponent, key, value)

            await session.commit()
            return exists_subcomponent

    async def deleteSubcomponent(self, subcomponent_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(Subcomponents).where(Subcomponents.id == subcomponent_id)
            )
            subcomponent = result.scalars().first()

            if subcomponent is None:
                return False

            await session.delete(subcomponent)
            await session.commit()
            return True

    async def getSubcomponentById(self, subcomponent_id: int) -> Subcomponents | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Subcomponents)
                .options(selectinload(Subcomponents.actividades))
                .where(Subcomponents.id == subcomponent_id)
            )
            subcomponent = statement.scalar_one_or_none()

            if subcomponent is None:
                return None

            return subcomponent
