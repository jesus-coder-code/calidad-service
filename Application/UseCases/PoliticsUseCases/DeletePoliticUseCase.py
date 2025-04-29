from Domain.Interfaces.IPoliticsRepository import IPoliticsRepository


class DeletePoliticUseCase:
    def __init__(self, politicsRepository: IPoliticsRepository):
        self.repository = politicsRepository

    async def execute(self, politic_id: int) -> bool:
        return await self.repository.deletePolitic(politic_id)
