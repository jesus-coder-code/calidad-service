from fastapi import APIRouter, Depends, Body
from Application.UseCases.AuthenticateUserUseCase import AuthenticateUserUseCase
from Domain.Interfaces.IAuthRepository import IAuthRepository
from Application.Schemas.AuthSchemas import AuthRequestSchema, TokenResponseSchema
from Infrastructure.utils.dependencies import verify_api_key
from Infrastructure.Repositories.AuthRepository import AuthRepository

router = APIRouter()


@router.post(
    "/token", response_model=TokenResponseSchema, dependencies=[Depends(verify_api_key)]
)
async def get_token(auth_request: AuthRequestSchema = Body(...)):
    auth_service = AuthRepository()
    use_case = AuthenticateUserUseCase(auth_service)
    return await use_case.execute(auth_request)
