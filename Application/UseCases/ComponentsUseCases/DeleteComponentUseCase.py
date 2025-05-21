from Domain.Interfaces.IComponentsRepository import IComponentsRepository


class DeleteComponentUseCase:
    def __init__(self, componentRepository: IComponentsRepository):
        self.repository = componentRepository

    async def execute(self, component_id: int) -> bool:
        return await self.repository.deleteComponent(component_id)
