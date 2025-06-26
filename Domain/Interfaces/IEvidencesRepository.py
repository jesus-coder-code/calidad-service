from abc import ABC, abstractmethod
from datetime import date
from Domain.Entities.Evidences import Evidences


class IEvidencesRepository(ABC):
    @abstractmethod
    async def createEvidence(self, evidences: Evidences) -> Evidences:
        pass

    @abstractmethod
    async def updateEvidence(
        self, evidence_id: int, created_at: date, avances: float
    ) -> Evidences | None:
        pass

    @abstractmethod
    async def deleteEvidence(self, evidence_id: int) -> bool:
        pass
