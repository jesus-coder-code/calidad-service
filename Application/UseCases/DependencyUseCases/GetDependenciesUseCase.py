from typing import List
from Domain.Interfaces.IDependencyRepository import IDependencyRepository
from Domain.Entities.Dependencies import Dependencies


class GetDependenciesUseCase:
    def __init__(self, dependencyRepository: IDependencyRepository):
        self.repository = dependencyRepository

    async def execute(self) -> List[Dependencies]:
        return await self.repository.getDependencies()
