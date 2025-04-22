from typing import List, Optional
from pydantic import BaseModel

from Application.Schemas.ActivitySchema import ActivitySchemaResponse


class ComponentSchema(BaseModel):
    nombre: str
    subcomponente: str

    class Config:
        from_attributes = True


class ComponentResponse(BaseModel):
    id: Optional[int]
    nombre: str
    subcomponente: str
    actividades: List[ActivitySchemaResponse] = []

    class Config:
        from_attributes = True


class ComponentSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    subcomponente: str
