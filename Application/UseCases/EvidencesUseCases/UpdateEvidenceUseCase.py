from datetime import date
from Domain.Interfaces.IEvidencesRepository import IEvidencesRepository
from Domain.Entities.Evidences import Evidences


class UpdateEvidenceUseCase:
    def __init__(self, evidencesRepository: IEvidencesRepository):
        self.repository = evidencesRepository

    async def execute(
        self, evidence_id: int, created_at: date, avances: float
    ) -> Evidences | None:
        return await self.repository.updateEvidence(evidence_id, created_at, avances)
