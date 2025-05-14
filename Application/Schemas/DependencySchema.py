from typing import List, Optional
from pydantic import BaseModel
from Application.Schemas.PoliticSchema import PoliticSchemaBaseResponse


class DependencyRequest(BaseModel):
    nombre: str

    class Config:
        from_attributes = True


class DependencyBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str

    class Config:
        from_attributes = True


class DependencyResponse(BaseModel):
    id: Optional[int]
    nombre: str
    politicas: List[PoliticSchemaBaseResponse] = []

    class Config:
        from_attributes = True
