from Domain.Entities.AuthEntity import AuthRequest, TokenResponse
from Domain.Interfaces.IAuthRepository import IAuthRepository


class AuthenticateUserUseCase:
    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository

    async def execute(self, auth_request: AuthRequest) -> TokenResponse:
        return await self.auth_repository.authenticate(auth_request)
