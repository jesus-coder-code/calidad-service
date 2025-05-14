from Domain.Entities.Dependencies import Dependencies
from Domain.Interfaces.IDependencyRepository import IDependencyRepository


class CreateDependencyUseCase:
    def __init__(self, dependencyRepository: IDependencyRepository):
        self.repository = dependencyRepository

    async def execute(self, dependency: Dependencies) -> Dependencies:
        return await self.repository.createDependency(dependency)
