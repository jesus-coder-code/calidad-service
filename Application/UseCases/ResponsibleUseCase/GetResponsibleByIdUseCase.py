from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository
from Domain.Entities.Responsible import Responsible


class GetResponsibleByIdUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self, responsible_id: int) -> Responsible | None:
        return await self.repository.getResposibleById(responsible_id)
