from typing import List
from sqlalchemy.orm import selectinload
from sqlmodel import select
from Domain.Entities.Components import Components
from Infrastructure.DB.Database import get_session
from Domain.Interfaces.IComponentsRepository import IComponentsRepository


class ComponentsRepository(IComponentsRepository):
    async def getAllComponents(self) -> List[Components]:
        async with get_session() as session:
            statement = select(Components).options(
                selectinload(Components.subcomponentes)
            )
            result = await session.execute(statement)
            return result.scalars().all()

    async def createComponent(self, components: Components) -> Components:
        async with get_session() as session:
            session.add(components)
            await session.commit()
            await session.refresh(components)
            return components

    async def updateComponent(
        self, component_id: int, components: Components
    ) -> Components | None:
        async with get_session() as session:
            component_found = await session.execute(
                select(Components).where(Components.id == component_id)
            )
            exists_component = component_found.scalar_one_or_none()

            if exists_component is None:
                return None

            for key, value in components.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(exists_component, key)
                ):
                    setattr(exists_component, key, value)

            await session.commit()
            return exists_component

    async def deleteComponent(self, component_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(Components).where(Components.id == component_id)
            )
            component = result.scalars().first()

            if component is None:
                return False

            await session.delete(component)
            await session.commit()
            return True

    async def getComponentById(self, component_id: int) -> Components | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Components)
                .options(selectinload(Components.subcomponentes))
                .where(Components.id == component_id)
            )

            component = statement.scalar_one_or_none()

            if component is None:
                return None

            return component
