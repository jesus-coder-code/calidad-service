from abc import ABC, abstractmethod
from Domain.Entities.AuthEntity import AuthRequest, TokenResponse


class IAuthRepository(ABC):
    @abstractmethod
    async def authenticate(self, auth_request: AuthRequest) -> TokenResponse:
        pass
