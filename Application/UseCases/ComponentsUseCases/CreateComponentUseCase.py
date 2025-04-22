from Domain.Interfaces.IComponentsRepository import IComponentsRepository
from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository
from Domain.Entities.Components import Components


class CreateComponentUseCase:
    def __init__(self, componentsRepository: IComponentsRepository):
        self.repository = componentsRepository

    async def execute(self, components: Components) -> Components:
        return await self.repository.createComponent(components)
