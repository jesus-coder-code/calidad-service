from fastapi import APIRouter, Depends, HTTPException
from Application.Schemas.AuthSchema import AuthResponse, AuthRequest
from Application.UseCases.AuthUseCases.AuthenticateUseCase import AuthenticateUseCase
from Infrastructure.Repositories.AuthRepository import AuthRepository
from Infrastructure.utils.auth import authenticate_user

router = APIRouter()


@router.post("/Auth")
async def login(auth_request: AuthRequest):
    try:
        tokens = authenticate_user(auth_request.username, auth_request.password)
        return {
            "access_token": tokens["AccessToken"],
            "id_token": tokens["IdToken"],
            "refresh_token": tokens.get("RefreshToken"),
        }
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
