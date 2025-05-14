from Domain.Entities.Dependencies import Dependencies
from Domain.Interfaces.IDependencyRepository import IDependencyRepository


class GetDependencyByIdUseCase:
    def __init__(self, dependencyRepository: IDependencyRepository):
        self.repository = dependencyRepository

    async def execute(self, dependency_id: int) -> Dependencies | None:
        return await self.repository.getDependencyById(dependency_id)
