from Domain.Entities.Components import Components
from Domain.Interfaces.IComponentsRepository import IComponentsRepository


class GetComponentByIdUseCase:
    def __init__(self, componentsRepository: IComponentsRepository):
        self.repository = componentsRepository

    async def execute(self, component_id: int) -> Components | None:
        return await self.repository.getComponentById(component_id)
