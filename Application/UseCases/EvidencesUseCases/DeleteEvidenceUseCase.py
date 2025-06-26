from Domain.Interfaces.IEvidencesRepository import IEvidencesRepository


class DeleteEvidencesUseCase:
    def __init__(self, evidencesRepository: IEvidencesRepository):
        self.repository = evidencesRepository

    async def execute(self, evidence_id: int) -> bool:
        return await self.repository.deleteEvidence(evidence_id)
