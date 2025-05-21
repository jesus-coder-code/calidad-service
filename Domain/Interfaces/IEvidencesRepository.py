from abc import ABC, abstractmethod
from Domain.Entities.Evidences import Evidences


class IEvidencesRepository(ABC):
    @abstractmethod
    async def createEvidence(self, evidences: Evidences) -> Evidences:
        pass
