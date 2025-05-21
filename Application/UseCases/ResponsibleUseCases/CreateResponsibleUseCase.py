from Domain.Entities.Responsible import Responsible
from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository


class CreateResponsibleUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self, responsible: Responsible) -> Responsible:
        return await self.repository.createResponsible(responsible)
