from Domain.Entities.Term import Term
from Domain.Interfaces.ITermRepository import ITermRepository


class GetTermByYearUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self, term_year: int) -> Term | None:
        return await self.repository.getTermByYear(term_year)
