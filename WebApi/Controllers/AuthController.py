from fastapi import APIRouter, Depends, HTTPException
from Application.Schemas.AuthSchema import AuthResponse, AuthRequest
from Application.UseCases.AuthUseCases.AuthenticateUseCase import AuthenticateUseCase
from Infrastructure.Repositories.AuthRepository import AuthRepository


router = APIRouter()


@router.post("/Auth", response_model=AuthResponse)
async def login(auth_request: AuthRequest):
    try:
        use_case = AuthenticateUseCase(AuthRepository())
        return await use_case.execute(auth_request)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
