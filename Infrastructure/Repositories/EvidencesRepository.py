from Domain.Entities.Evidences import Evidences
from sqlmodel.ext.asyncio.session import AsyncSession

from Domain.Interfaces.IEvidencesRepository import IEvidencesRepository
from Infrastructure.DB.Database import get_session


class EvidencesRepository(IEvidencesRepository):
    async def createEvidence(self, evidences: Evidences) -> Evidences:
        async with get_session() as session:
            session.add(evidences)
            await session.commit()
            await session.refresh(evidences)
            return evidences
