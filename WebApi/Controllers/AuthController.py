from fastapi import APIRouter, Depends, HTTPException, Header
from Application.Schemas.AuthSchema import (
    AuthRequest,
    RegisterRequest,
    ConfirmRequest,
    PasswordResetRequest,
    ConfirmPasswordResetRequest,
    ChangePasswordRequest,
)
from Infrastructure.utils.auth import (
    authenticate_user,
    register_user,
    confirm_user,
    send_password_reset_code,
    confirm_new_password,
    change_password,
)
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


@router.post("/Auth/Confirm", dependencies=[Depends(verify_api_key)])
async def confirm_email(confirm_request: ConfirmRequest):
    try:
        confirm_user(confirm_request.email, confirm_request.code)
        return {"message": "Cuenta confirmada exitosamente."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/Auth/Recover", dependencies=[Depends(verify_api_key)])
async def recover_password(reset_request: PasswordResetRequest):
    try:
        send_password_reset_code(reset_request.email)
        return {"message": "Código de recuperación enviado al correo."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/Auth/Reset", dependencies=[Depends(verify_api_key)])
async def reset_password(confirm_request: ConfirmPasswordResetRequest):
    try:
        confirm_new_password(
            username=confirm_request.email,
            confirmation_code=confirm_request.code,
            new_password=confirm_request.new_password,
        )
        return {"message": "Contraseña restablecida correctamente."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


"""@router.post("/Auth/ChangePassword", dependencies=[Depends(verify_api_key)])
async def change_user_password(
    request: ChangePasswordRequest,
    authorization: str = Header(..., alias="Authorization"),
):
    try:
        access_token = authorization.replace("Bearer ", "")
        change_password(
            access_token=access_token,
            old_password=request.old_password,
            new_password=request.new_password,
        )
        return {"message": "Contraseña actualizada correctamente."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))"""
