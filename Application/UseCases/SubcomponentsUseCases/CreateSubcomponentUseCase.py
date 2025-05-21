from Domain.Interfaces.ISubcomponentsRepository import ISubcomponentsRepository
from Domain.Entities.Subcomponents import Subcomponents


class CreateSubcomponentUseCase:
    def __init__(self, subcomponentsRepository: ISubcomponentsRepository):
        self.repository = subcomponentsRepository

    async def execute(self, subcomponent: Subcomponents) -> Subcomponents:
        return await self.repository.createSubcomponent(subcomponent)
