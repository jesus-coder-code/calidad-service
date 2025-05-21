from pydantic import BaseModel
from typing import Optional, List

from Application.Schemas.ActionPlanSchema import ActionPlanSchemaResponse
from Application.Schemas.ComponentSchema import ComponentResponse


class PoliticSchemaRequest(BaseModel):
    nombre: str
    responsable_id: Optional[int]
    dependencia_id: Optional[int] = None

    class Config:
        from_attributes = True


class PoliticSchemaBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str
    responsable_id: Optional[int]
    dependencia_id: Optional[int]

    class Config:
        from_attributes = True


class PoliticSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    dependencia_id: Optional[int]
    planes: List[ActionPlanSchemaResponse] = []
    componentes: List[ComponentResponse] = []

    class Config:
        from_attributes = True
