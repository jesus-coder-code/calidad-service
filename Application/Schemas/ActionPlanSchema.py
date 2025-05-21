from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from Application.Schemas.ActivitySchema import (
    ActivityBaseResponse,
    ActivitySummaryResponse,
)


class ActionPlanResponse(BaseModel):
    id: Optional[int]
    nombre: str
    vigencia_id: int
    politica_id: int
    actividades: List[ActivitySummaryResponse] = []

    class Config:
        from_attributes = True


class ActionPlanSchema(BaseModel):
    nombre: str
    vigencia_id: int
    politica_id: int

    class Config:
        from_attributes = True


class ActionPlanSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    vigencia_id: int
    politica_id: int

    class Config:
        from_attributes = True
