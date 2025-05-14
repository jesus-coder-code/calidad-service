from abc import ABC, abstractmethod
from Domain.Entities.Dependencies import Dependencies
from typing import List


class IDependencyRepository(ABC):
    @abstractmethod
    async def getDependencies(self) -> List[Dependencies]:
        pass

    @abstractmethod
    async def createDependency(self, dependency: Dependencies) -> Dependencies:
        pass

    @abstractmethod
    async def updateDependency(
        self, dependency_id: int, dependency: Dependencies
    ) -> Dependencies | None:
        pass

    @abstractmethod
    async def deleteDependency(self, dependency_id: int) -> bool:
        pass

    @abstractmethod
    async def getDependencyById(self, dependency_id: int) -> Dependencies | None:
        pass
