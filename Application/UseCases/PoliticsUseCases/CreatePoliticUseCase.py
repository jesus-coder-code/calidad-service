from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository
from Domain.Entities.Politics import Politics


class CreatePoliticUseCase:
    def __init__(self, politicsRepository: IPoliticsRepository):
        self.repository = politicsRepository

    async def execute(self, politics: Politics) -> Politics:
        return await self.repository.createPolitic(politics)
