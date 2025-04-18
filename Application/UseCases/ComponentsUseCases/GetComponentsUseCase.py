from typing import List
from Domain.Entities.Components import Components
from Infrastructure.Repositories.ComponentsRepository import ComponentsRepository


class GetComponentsUseCase:
    def __init__(self):
        self.repository = ComponentsRepository()

    async def execute(self) -> List[Components]:
        return await self.repository.getAllComponents()
