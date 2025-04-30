from pydantic import BaseModel
from typing import Optional, List

from Application.Schemas.ActionPlanSchema import ActionPlanSchemaResponse
from Application.Schemas.ComponentSchema import ComponentSchemaBaseResponse


class PoliticSchemaRequest(BaseModel):
    nombre: str

    class Config:
        from_attributes = True


class PoliticSchemaBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str

    class Config:
        from_attributes = True


class PoliticSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    planes: List[ActionPlanSchemaResponse] = []
    componentes: List[ComponentSchemaBaseResponse] = []

    class Config:
        from_attributes = True
