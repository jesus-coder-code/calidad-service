from Domain.Interfaces.IDependencyRepository import IDependencyRepository
from Domain.Entities.Dependencies import Dependencies


class UpdateDependencyUseCase:
    def __init__(self, dependencyRepository: IDependencyRepository):
        self.repository = dependencyRepository

    async def execute(
        self, dependency_id: int, dependency: Dependencies
    ) -> Dependencies | None:
        return await self.repository.updateDependency(dependency_id, dependency)
