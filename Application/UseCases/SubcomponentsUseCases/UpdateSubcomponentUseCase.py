from Domain.Entities.Subcomponents import Subcomponents
from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository


class UpdateSubcomponentUseCase:
    def __init__(self, subcomponentRepository: ISubcomponentsRepository):
        self.repository = subcomponentRepository

    async def execute(
        self, subcomponent_id: int, subcomponent: Subcomponents
    ) -> Subcomponents | None:
        return await self.repository.updateSubcomponent(subcomponent_id, subcomponent)
