import httpx
from typing import Optional
from Domain.Entities.AuthEntity import AuthRequest, TokenResponse
from Domain.Interfaces.IAuthRepository import IAuthRepository
from Infrastructure.utils.configuration import settings
from fastapi import HTTPException, status


class AuthRepository(IAuthRepository):
    def __init__(self):
        self.token_endpoint = settings.COGNITO_ENDPOINT
        self.client_id = settings.COGNITO_CLIENT_ID
        self.client_secret = settings.COGNITO_CLIENT_SECRET

    async def authenticate(self, auth_request: AuthRequest) -> TokenResponse:
        auth_data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": auth_request.username,
            "password": auth_request.password,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.token_endpoint, data=auth_data, headers=headers
                )
                response.raise_for_status()
                return TokenResponse(data=response.json())

        except httpx.HTTPStatusError as e:
            error_detail = (
                "Invalid credentials"
                if e.response.status_code == 401
                else "Authentication failed"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=error_detail
            ) from e

        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Authentication service unavailable",
            ) from e

        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal error",
            ) from e
