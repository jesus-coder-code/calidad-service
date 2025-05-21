from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository
from Domain.Entities.Politics import Politics


class UpdatePoliticUseCase:
    def __init__(self, politicsRepository: IPoliticsRepository):
        self.repository = politicsRepository

    async def execute(self, politic_id: int, politics: Politics) -> Politics | None:
        return await self.repository.updatePolitic(politic_id, politics)
