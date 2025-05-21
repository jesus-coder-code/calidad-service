from Domain.Entities.Subcomponents import Subcomponents
from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository


class GetSubcomponentByIdUseCase:
    def __init__(self, subcomponentsRepository: ISubcomponentsRepository):
        self.repository = subcomponentsRepository

    async def execute(self, subcomponent_id: int) -> Subcomponents | None:
        return await self.repository.getSubcomponentById(subcomponent_id)
