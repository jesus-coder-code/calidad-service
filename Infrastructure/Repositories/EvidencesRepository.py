from datetime import date

from sqlmodel import select

from Domain.Entities.Evidences import Evidences
from sqlmodel.ext.asyncio.session import AsyncSession
from Infrastructure.utils.evidence import delete_file_from_s3

from Domain.Interfaces.IEvidencesRepository import IEvidencesRepository
from Infrastructure.DB.Database import get_session


class EvidencesRepository(IEvidencesRepository):
    async def createEvidence(self, evidences: Evidences) -> Evidences:
        async with get_session() as session:
            session.add(evidences)
            await session.commit()
            await session.refresh(evidences)
            return evidences

    async def updateEvidence(
        self, evidence_id: int, created_at: date, avances: float
    ) -> Evidences | None:
        async with get_session() as session:
            result = await session.execute(
                select(Evidences).where(Evidences.id == evidence_id)
            )
            evidence = result.scalar_one_or_none()

            if evidence is None:
                return None

            evidence.created_at = created_at
            evidence.avances = avances

            await session.commit()
            return evidence

    async def deleteEvidence(self, evidence_id: int) -> bool:
        async with get_session() as session:
            result = await session.execute(
                select(Evidences).where(Evidences.id == evidence_id)
            )
            evidence = result.scalar_one_or_none()

            if evidence is None:
                return False

            actividad_id = evidence.actividad_id
            filename = evidence.nombre_archivo
            try:
                delete_file_from_s3(actividad_id, filename)
            except Exception as e:
                print(f"error al eliminar el archivo del bucket: {str(e)}")

            await session.delete(evidence)
            await session.commit()
            return True
