from abc import ABC, abstractmethod
from Domain.Entities.Responsible import Responsible
from typing import List


class IResponsibleRepository(ABC):
    @abstractmethod
    async def getAllResponsible(self) -> List[Responsible]:
        pass

    @abstractmethod
    async def createResponsible(self, responsible: Responsible) -> Responsible:
        pass

    @abstractmethod
    async def updateResponsible(
        self, responsible_id: int, responsible: Responsible
    ) -> Responsible | None:
        pass

    @abstractmethod
    async def deleteResponsible(self, responsible_id: int) -> bool:
        pass

    @abstractmethod
    async def getResposibleById(self, responsible_id: int) -> Responsible | None:
        pass

    @abstractmethod
    async def getResponsibleByName(self, responsible_name: str) -> Responsible | None:
        pass

    @abstractmethod
    async def getResponsibleByEmail(self, responsible_email: str) -> Responsible | None:
        pass
