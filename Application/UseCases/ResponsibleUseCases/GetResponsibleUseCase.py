from typing import List
from Domain.Entities.Responsible import Responsible
from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository


class GetResponsibleUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self) -> List[Responsible]:
        return await self.repository.getAllResponsible()
