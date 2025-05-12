from Domain.Entities.Term import Term
from Domain.Interfaces.ITermRepository import ITermRepository
from Infrastructure.DB.Database import get_session
from sqlmodel import select
from sqlalchemy.orm import selectinload
from typing import List


class TermRepository(ITermRepository):
    async def getAllTerms(self) -> List[Term]:
        async with get_session() as session:
            statement = select(Term).options(selectinload(Term.planes))
            result = await session.execute(statement)
            return result.scalars().all()

    async def createTerm(self, term: Term) -> Term:
        async with get_session() as session:
            session.add(term)
            await session.commit()
            await session.refresh(term)
            return term

    async def updateTerm(self, term_id: int, term: Term) -> Term | None:
        raise NotImplementedError

    async def deleteTerm(self, term_id: int) -> bool:
        async with get_session() as session:
            statement = await session.execute(select(Term).where(Term.id == term_id))
            term = statement.scalars().first()

            if term is None:
                return False

            await session.delete(term)
            await session.commit()
            return True

    async def getTermById(self, term_id: int) -> Term | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Term)
                .options(selectinload(Term.planes))
                .where(Term.id == term_id)
            )

            term = statement.scalar_one_or_none()
            if term is None:
                return None
            return term
