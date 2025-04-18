from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository
from Domain.Entities.Components import Components


class CreateComponentUseCase:
    def __init__(self):
        self.repository = ComponentsRepository()

    async def execute(self, components: Components) -> Components:
        return await self.repository.createComponent(components)
