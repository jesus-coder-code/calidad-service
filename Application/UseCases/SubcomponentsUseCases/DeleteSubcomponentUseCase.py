from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository
from Domain.Entities.Subcomponents import Subcomponents


class DeleteSubcomponentUseCase:
    def __init__(self, subcomponentsRepository: ISubcomponentsRepository):
        self.repository = subcomponentsRepository

    async def execute(self, subcomponent_id: int) -> bool:
        return await self.repository.deleteSubcomponent(subcomponent_id)
