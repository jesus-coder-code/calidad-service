from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository
from Domain.Entities.Politics import Politics
from Domain.Entities.Components import Components
from typing import List
from Infrastructure.DB.Database import get_session
from sqlmodel import select
from sqlalchemy.orm import selectinload


class PoliticsRepository(IPoliticsRepository):
    async def getAllPolitics(self) -> List[Politics]:
        async with get_session() as session:
            statement = select(Politics).options(
                selectinload(Politics.responsable),
                selectinload(Politics.planes),
                selectinload(Politics.componentes).selectinload(
                    Components.subcomponentes
                ),
            )
            result = await session.execute(statement)
            return result.scalars().all()

    async def createPolitic(self, politics: Politics) -> Politics:
        async with get_session() as session:
            session.add(politics)
            await session.commit()
            await session.refresh(politics)
            return politics

    async def updatePolitic(
        self, politic_id: int, politics: Politics
    ) -> Politics | None:
        async with get_session() as session:
            politic_found = await session.execute(
                select(Politics).where(Politics.id == politic_id)
            )
            exists_politic = politic_found.scalar_one_or_none()

            if exists_politic is None:
                return None

            for key, value in politics.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(exists_politic, key)
                ):
                    setattr(exists_politic, key, value)

            await session.commit()
            return exists_politic

    async def deletePolitic(self, politic_id: int) -> bool:
        raise NotImplementedError

    async def getPoliticById(self, politic_id: int) -> Politics | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Politics)
                .options(
                    selectinload(Politics.responsable),
                    selectinload(Politics.planes),
                    selectinload(Politics.componentes).selectinload(
                        Components.subcomponentes
                    ),
                )
                .where(Politics.id == politic_id)
            )

            politic = statement.scalar_one_or_none()

            if politic is None:
                return None

            return politic
