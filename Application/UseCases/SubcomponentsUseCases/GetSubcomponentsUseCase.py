from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository
from typing import List
from Domain.Entities.Subcomponents import Subcomponents


class GetSubcomponentsUseCase:
    def __init__(self, subcomponentsRepository: ISubcomponentsRepository):
        self.repository = subcomponentsRepository

    async def execute(self) -> List[Subcomponents]:
        return await self.repository.getAllSubcomponents()
