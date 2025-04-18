from typing import List
from sqlalchemy.orm import selectinload
from sqlmodel import select
from Domain.Entities.Components import Components
from Infrastructure.DB.Database import get_session


class ComponentsRepository:
    async def getAllComponents(self) -> List[Components]:
        async with get_session() as session:
            statement = statement = select(Components).options(
                selectinload(Components.actividades)
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
