from Domain.Interfaces.ITermRepository import ITermRepository
from Domain.Entities.Term import Term


class CreateTermUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self, term: Term) -> Term | bool:
        return await self.repository.createTerm(term)
