from typing import Dict
from pydantic import BaseModel, ConfigDict


#se define la entidad para el login y los tipos de datos que llegarán a esta
class AuthRequest(BaseModel):
    username: str
    password: str

#
class TokenResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    data: Dict[str, any]