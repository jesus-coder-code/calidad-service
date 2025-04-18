from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository
from Domain.Entities.Components import Components


class UpdateComponentsUseCase:
    def __init__(self):
        self.repository = ComponentsRepository()

    async def execute(
        self, component_id: int, update_component: Components
    ) -> Components | None:
        return await self.repository.updateComponent(component_id, update_component)
