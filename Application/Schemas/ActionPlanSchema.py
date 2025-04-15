from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from Application.Schemas.ActivitySchema import ActivitySchema


"""class ActivityResponse(BaseModel):
    id: Optional[int]
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    plan_id: Optional[int]

    class Config:
        from_attributes = True"""


class ActionPlanResponse(BaseModel):
    id: Optional[int]
    nombre: str
    vigencia: int
    actividades: List[ActivitySchema] = []

    class Config:
        from_attributes = True
