from Application.Schemas.AuthSchema import AuthRequest, AuthResponse
from Domain.Interfaces.IAuthRepository import IAuthRepository
from typing import Any


class AuthenticateUseCase:
    def __init__(self, authRepository: IAuthRepository):
        self.repository = authRepository

    async def execute(self, request: AuthRequest) -> Any:
        token_data = await self.repository.authenticate(
            request.username, request.password
        )
        return token_data
