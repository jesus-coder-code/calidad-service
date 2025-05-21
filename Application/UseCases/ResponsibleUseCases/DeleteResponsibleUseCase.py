from Domain.Interfaces.IResponsibleRepository import IResponsibleRepository


class DeleteResponsibleUseCase:
    def __init__(self, responsibleRepository: IResponsibleRepository):
        self.repository = responsibleRepository

    async def execute(self, responsible_id: int) -> bool:
        return await self.repository.deleteResponsible(responsible_id)
