from pydantic import BaseModel, ConfigDict
from typing import Any, Dict


class AuthRequestSchema(BaseModel):
    username: str
    password: str


class TokenResponseSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    data: Dict[str, Any]
