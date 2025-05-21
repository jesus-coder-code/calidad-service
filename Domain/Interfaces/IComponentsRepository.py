from abc import ABC, abstractmethod
from typing import List
from Domain.Entities.Components import Components


class IComponentsRepository(ABC):
    @abstractmethod
    async def getAllComponents(self) -> List[Components]:
        pass

    @abstractmethod
    async def createComponent(self, components: Components) -> Components:
        pass

    @abstractmethod
    async def updateComponent(
        self, component_id: int, components: Components
    ) -> Components | None:
        pass

    @abstractmethod
    async def deleteComponent(self, component_id: int) -> bool:
        pass

    @abstractmethod
    async def getComponentById(self, component_id: int) -> Components | None:
        pass
