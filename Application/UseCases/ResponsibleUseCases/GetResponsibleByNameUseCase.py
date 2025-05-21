from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository
from Domain.Entities.Responsible import Responsible


class GetResponsibleByNameUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self, responsible_name: str) -> Responsible | None:
        return await self.repository.getResponsibleByName(responsible_name)
