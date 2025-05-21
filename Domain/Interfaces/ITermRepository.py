from abc import ABC, abstractmethod
from typing import List
from Domain.Entities.Term import Term


class ITermRepository(ABC):
    @abstractmethod
    async def getAllTerms(self) -> List[Term]:
        pass

    @abstractmethod
    async def createTerm(self, term: Term) -> Term | bool:
        pass

    @abstractmethod
    async def updateTerm(self, term_id: int, term: Term) -> Term | None:
        pass

    @abstractmethod
    async def deleteTerm(self, term_id: int) -> bool:
        pass

    @abstractmethod
    async def getTermByYear(self, term_year: int) -> Term | None:
        pass
