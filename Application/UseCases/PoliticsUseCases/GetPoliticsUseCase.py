from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository
from Domain.Entities.Politics import Politics
from typing import List


class GetPoliticsUseCase:
    def __init__(self, politicsRepository: IPoliticsRepository):
        self.repository = politicsRepository

    async def execute(self) -> List[Politics]:
        return await self.repository.getAllPolitics()
