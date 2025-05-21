from Domain.Interfaces.IDependencyRepository import IDependencyRepository


class DeleteDependencyUseCase:
    def __init__(self, dependencyRepository: IDependencyRepository):
        self.repository = dependencyRepository

    async def execute(self, dependency_id: int) -> bool:
        return await self.repository.deleteDependency(dependency_id)
