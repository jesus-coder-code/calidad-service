import httpx
from Domain.Interfaces.IAuthRepository import IAuthRepository
from Infrastructure.utils.configuration import *


class AuthRepository(IAuthRepository):
    def __init__(self):
        self.token_url = COGNITO_TOKEN_URL
        self.client_id = COGNITO_CLIENT_ID
        self.client_secret = COGNITO_CLIENT_SECRET

    async def authenticate(self, username: str, password: str) -> dict | None:
        data = {
            "grant-type": "password",
            "client_id": self.client_id,
            "username": username,
            "password": password,
        }

        auth = (self.client_id, self.client_secret)

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.token_url, data=data, auth=auth, headers=headers
            )

            print(response)
            if response.status_code != 200:
                raise Exception(f"Authentication failed: {response.text}")

            return response.json()
