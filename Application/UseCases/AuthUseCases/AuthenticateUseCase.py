from Application.Schemas.AuthSchema import AuthRequest, AuthResponse
from Domain.Interfaces.IAuthRepository import IAuthRepository


class AuthenticateUseCase:
    def __init__(self, authRepository: IAuthRepository):
        self.repository = authRepository

    async def execute(self, request: AuthRequest) -> AuthResponse:
        token_data = await self.repository.authenticate(request.email, request.password)
        return AuthResponse(**token_data)
