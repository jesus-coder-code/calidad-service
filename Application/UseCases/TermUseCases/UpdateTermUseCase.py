from Domain.Entities.Term import Term
from Domain.Interfaces.ITermRepository import ITermRepository


class UpdateTermUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self, term_id: int, term: Term) -> Term | None:
        return await self.repository.updateTerm(term_id, term)
