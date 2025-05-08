from sqlmodel import select
from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository
from typing import List
from Domain.Entities.Responsible import Responsible
from Infrastructure.DB.Database import get_session


class ResponsibleRepository(IResponsibleRepository):
    async def getAllResponsible(self) -> List[Responsible]:
        async with get_session() as session:
            statement = select(Responsible)
            result = await session.execute(statement)
            return result.scalars().all()

    async def createResponsible(self, responsible: Responsible) -> Responsible:
        async with get_session() as session:
            session.add(responsible)
            await session.commit()
            await session.refresh(responsible)
            return responsible

    async def updateResponsible(
        self, responsible_id: int, responsible: Responsible
    ) -> Responsible | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Responsible).where(Responsible.id == responsible_id)
            )
            exists_responsible = statement.scalar_one_or_none()

            if exists_responsible is None:
                return None

            for key, value in responsible.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(exists_responsible, key)
                ):
                    setattr(exists_responsible, key, value)

            await session.commit()
            return exists_responsible

    async def deleteResponsible(self, responsible_id: int) -> bool:
        async with get_session() as session:
            statement = await session.execute(
                select(Responsible).where(Responsible.id == responsible_id)
            )
            responsible = statement.scalars().first()

            if responsible is None:
                return False

            await session.delete(responsible)
            await session.commit()
            return True

    async def getResposibleById(self, responsible_id: int) -> Responsible:
        async with get_session() as session:
            statement = await session.execute(
                select(Responsible).where(Responsible.id == responsible_id)
            )
            existing_responsible = statement.scalar_one_or_none()

            if existing_responsible is None:
                return None

            return existing_responsible

    async def getResponsibleByName(self, responsible_name: str) -> Responsible | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Responsible).where(Responsible.id == responsible_name)
            )
            existing_responsible = statement.scalar_one_or_none()

            if existing_responsible is None:
                return None

            return existing_responsible
