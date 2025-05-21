from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository
from Domain.Entities.Components import Components
from Domain.Interfaces.IComponentsRepository import IComponentsRepository


class UpdateComponentsUseCase:
    def __init__(self, componentsRepository: IComponentsRepository):
        self.repository = componentsRepository

    async def execute(
        self, component_id: int, update_component: Components
    ) -> Components | None:
        return await self.repository.updateComponent(component_id, update_component)
