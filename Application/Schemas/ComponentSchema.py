from typing import List, Optional
from pydantic import BaseModel

from Application.Schemas.SubcomponentSchema import SubcomponentSchemaResponse


class ComponentSchema(BaseModel):
    nombre: str
    politica_id: int

    class Config:
        from_attributes = True


class ComponentResponse(BaseModel):
    id: Optional[int]
    nombre: str
    politica_id: int
    subcomponentes: List[SubcomponentSchemaResponse] = []

    class Config:
        from_attributes = True


class ComponentSchemaBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str
    politica_id: int

    class Config:
        from_attributes = True
