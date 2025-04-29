from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository
from Domain.Entities.Politics import Politics
from typing import List
from Infrastructure.DB.Database import get_session


class PoliticsRepository(IPoliticsRepository):
    async def getAllPolitics(self) -> List[Politics]:
        raise NotImplementedError

    async def createPolitic(self, politics: Politics) -> Politics:
        raise NotImplementedError

    async def updatePolitic(
        self, politic_id: int, politics: Politics
    ) -> Politics | None:
        raise NotImplementedError

    async def deletePolitic(self, politic_id: int) -> bool:
        raise NotImplementedError
