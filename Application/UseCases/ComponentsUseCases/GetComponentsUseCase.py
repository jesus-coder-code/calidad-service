from typing import List
from Domain.Entities.Components import Components
from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository
from Domain.Interfaces.IComponentsRepository import IComponentsRepository


class GetComponentsUseCase:
    def __init__(self, componentsRepository: IComponentsRepository):
        self.repository = componentsRepository

    async def execute(self) -> List[Components]:
        return await self.repository.getAllComponents()
