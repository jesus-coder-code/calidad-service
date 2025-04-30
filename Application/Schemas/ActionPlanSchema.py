from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from Application.Schemas.ActivitySchema import ActivitySchemaResponse


class ActionPlanResponse(BaseModel):
    id: Optional[int]
    nombre: str
    vigencia: int
    actividades: List[ActivitySchemaResponse] = []

    class Config:
        from_attributes = True


class ActionPlanSchema(BaseModel):
    nombre: str
    vigencia: int
    politica_id: int

    class Config:
        from_attributes = True


class ActionPlanSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    vigencia: int
    politica_id: int

    class Config:
        from_attributes = True
