from Domain.Interfaces.ITermRepository import ITermRepository


class DeleteTermUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self, term_id: int) -> bool:
        return await self.repository.deleteTerm(term_id)
