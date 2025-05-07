from abc import ABC, abstractmethod
from typing import List
from Domain.Entities.Subcomponents import Subcomponents


class ISubcomponentsRepository(ABC):
    @abstractmethod
    async def getAllSubcomponents(self) -> List[Subcomponents]:
        pass

    @abstractmethod
    async def createSubcomponent(self, subcomponents: Subcomponents) -> Subcomponents:
        pass

    @abstractmethod
    async def updateSubcomponent(
        self, subcomponent_id: int, subcomponents: Subcomponents
    ) -> Subcomponents | None:
        pass

    @abstractmethod
    async def deleteSubcomponent(self, subcomponent_id: int) -> bool:
        pass

    @abstractmethod
    async def getSubcomponentById(self, subcomponent_id: int) -> Subcomponents | None:
        pass
