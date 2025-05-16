from pydantic import BaseModel
from typing import List, Optional

from Application.Schemas.ActivitySchema import ActivityBaseResponse


class SubcomponentSchema(BaseModel):
    nombre: str
    component_id: int

    class Config:
        from_attributes = True


class SubcomponentSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    component_id: int

    class Config:
        from_attributes = True


class SubcomponentBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str
    component_id: Optional[int]
    actividades: List[ActivityBaseResponse] = []

    class Config:
        from_attributes = True
