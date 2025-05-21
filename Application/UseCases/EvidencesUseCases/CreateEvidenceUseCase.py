from Domain.Interfaces.IEvidencesRepository import IEvidencesRepository
from Domain.Entities.Evidences import Evidences


class CreateEvidenceUseCase:
    def __init__(self, evidencesRepository: IEvidencesRepository):
        self.repository = evidencesRepository

    async def execute(self, evidences: Evidences) -> Evidences:
        return await self.repository.createEvidence(evidences)
