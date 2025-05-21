from fastapi import APIRouter, Depends, HTTPException
from Application.Schemas.AuthSchema import AuthRequest, RegisterRequest
from Infrastructure.utils.auth import authenticate_user, register_user
from Infrastructure.utils.verifyApiKey import verify_api_key

router = APIRouter()


@router.post("/Auth", dependencies=[Depends(verify_api_key)])
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


@router.post("/Auth/Register", dependencies=[Depends(verify_api_key)])
async def register(auth_request: RegisterRequest):
    try:
        response = register_user(
            username=auth_request.email,
            name=auth_request.name,
            password=auth_request.password,
        )
        return {
            "message": "Usuario registrado correctamente. Confirme por email.",
            "response": response,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
