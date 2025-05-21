from abc import ABC, abstractmethod
from typing import List
from Domain.Entities.Politics import Politics


class IPoliticsRepository(ABC):
    @abstractmethod
    async def getAllPolitics(self) -> List[Politics]:
        pass

    @abstractmethod
    async def createPolitic(self, politics: Politics) -> Politics:
        pass

    @abstractmethod
    async def updatePolitic(
        self, politic_id: int, politics: Politics
    ) -> Politics | None:
        pass

    @abstractmethod
    async def deletePolitic(self, politic_id: int) -> bool:
        pass

    @abstractmethod
    async def getPoliticById(self, politic_id: int) -> Politics | None:
        pass
