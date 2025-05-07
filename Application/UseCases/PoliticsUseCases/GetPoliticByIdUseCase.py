from Domain.Entities.Politics import Politics
from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository


class GetPoliticByIdUseCase:
    def __init__(self, politicsRepository: IPoliticsRepository):
        self.repository = politicsRepository

    async def execute(self, politic_id: int) -> Politics | None:
        return await self.repository.getPoliticById(politic_id)
