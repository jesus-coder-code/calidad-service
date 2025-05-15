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

    async def createTerm(self, term: Term) -> Term | bool:
        async with get_session() as session:
            statement = await session.execute(
                select(Term).where(Term.vigencia == term.vigencia)
            )
            result = statement.scalar_one_or_none()
            print(statement)
            if result is None:
                session.add(term)
                await session.commit()
                await session.refresh(term)
                return term
            else:
                return False

    async def updateTerm(self, term_id: int, term: Term) -> Term | None:
        async with get_session() as session:
            statement = await session.execute(select(Term).where(Term.id == term_id))
            existing_term = statement.scalars().first()

            if existing_term is None:
                return None

            for key, value in term.__dict__.items():
                if (
                    key != "id"
                    and key != "_sa_instance_state"
                    and hasattr(existing_term, key)
                ):
                    setattr(existing_term, key, value)

            await session.commit()
            return existing_term

    async def deleteTerm(self, term_id: int) -> bool:
        async with get_session() as session:
            statement = await session.execute(select(Term).where(Term.id == term_id))
            term = statement.scalars().first()

            if term is None:
                return False

            await session.delete(term)
            await session.commit()
            return True

    async def getTermByYear(self, term_year: int) -> Term | None:
        async with get_session() as session:
            statement = await session.execute(
                select(Term)
                .options(selectinload(Term.planes))
                .where(Term.vigencia == term_year)
            )

            term = statement.scalar_one_or_none()
            if term is None:
                return None
            return term
