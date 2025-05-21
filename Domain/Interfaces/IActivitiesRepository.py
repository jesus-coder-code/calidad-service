from abc import ABC, abstractmethod
from typing import List

from Domain.Entities.Activities import Activities


class IActivitiesRepository(ABC):
    @abstractmethod
    async def getAllActivities(self) -> List[Activities]:
        pass

    @abstractmethod
    async def createActivity(self, activities: Activities) -> Activities:
        pass

    @abstractmethod
    async def updateActivity(
        self, activity_id: int, activities: Activities
    ) -> Activities | None | bool:
        pass

    @abstractmethod
    async def deleteActivity(self, activity_id: int) -> bool:
        pass

    @abstractmethod
    async def getActivityById(self, activity_id: int) -> Activities | None:
        pass

    @abstractmethod
    async def getActivityByName(self, activity_name: str) -> Activities | None:
        pass
