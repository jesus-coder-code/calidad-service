from Domain.Interfaces.IDependencyRepository import IDependencyRepository
from Domain.Entities.Dependencies import Dependencies
from typing import List
from Infrastructure.DB.Database import get_session
from sqlalchemy.orm import selectinload
from sqlmodel import select


class DependencyRepository(IDependencyRepository):
    async def getDependencies(self) -> List[Dependencies]:
        async with get_session() as session:
            statement = select(Dependencies).options(
                selectinload(Dependencies.responsable),
                selectinload(Dependencies.politicas),
            )
            result = await session.execute(statement)
            return result.scalars().all()

    async def createDependency(self, dependency: Dependencies) -> Dependencies:
        async with get_session() as session:
            session.add(dependency)
            await session.commit()
            await session.refresh(dependency)
            return dependency

    async def updateDependency(
        self, dependency_id: int, dependency: Dependencies
    ) -> Dependencies | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Dependencies).where(Dependencies.id == dependency_id)
            )
            existing_dependency = statement.scalars().first()

            if existing_dependency is None:
                return None

            for key, value in dependency.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(existing_dependency, key)
                ):
                    setattr(existing_dependency, key, value)

            await session.commit()
            return existing_dependency

    async def deleteDependency(self, dependency_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(Dependencies).where(Dependencies.id == dependency_id)
            )
            dependency = result.scalars().first()

            if dependency is None:
                return False

            await session.delete(dependency)
            await session.commit()
            return True

    async def getDependencyById(self, dependency_id: int) -> Dependencies | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Dependencies)
                .options(
                    selectinload(Dependencies.politicas),
                    selectinload(Dependencies.responsable),
                )
                .where(Dependencies.id == dependency_id)
            )

            existing_dependency = statement.scalar_one_or_none()

            if existing_dependency is None:
                return None

            return existing_dependency
