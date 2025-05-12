from Domain.Entities.Term import Term
from Domain.Interfaces.ITermRepository import ITermRepository


class GetTermByIdUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self, term_id: int) -> Term | None:
        return await self.repository.getTermById(term_id)
