from typing import List
from Domain.Entities.Term import Term
from Domain.Interfaces.ITermRepository import ITermRepository


class GetAllTermsUseCase:
    def __init__(self, termRepository: ITermRepository):
        self.repository = termRepository

    async def execute(self) -> List[Term]:
        return await self.repository.getAllTerms()
