from abc import ABC, abstractmethod


class IAuthRepository(ABC):
    @abstractmethod
    async def authenticate(self, email: str, password: str) -> dict | None:
        pass
