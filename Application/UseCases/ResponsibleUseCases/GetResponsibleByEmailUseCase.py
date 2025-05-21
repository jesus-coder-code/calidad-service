from Domain.Entities.Responsible import Responsible
from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository


class GetResponsibleByEmailUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self, responsible_email: str) -> Responsible | None:
        return await self.repository.getResponsibleByEmail(responsible_email)
