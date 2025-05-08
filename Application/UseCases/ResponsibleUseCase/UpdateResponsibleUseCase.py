from Domain.Entities.Responsible import Responsible
from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository


class UpdateResponsibleUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(
        self, responsible_id: int, responsible: Responsible
    ) -> Responsible | None:
        return await self.repository.updateResponsible(responsible_id, responsible)
