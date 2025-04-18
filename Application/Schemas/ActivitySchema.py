from typing import Optional
from pydantic import BaseModel
from datetime import date

from Domain.Enums.CicloEnum import CicloEnum


class ActivitySchema(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum
    plan_id: int
    component_id: int

    class Config:
        from_attributes = True
        use_enum_values = True


class ActivitySchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum
    plan_id: int
    component_id: int

    class Config:
        from_attributes = True
        use_enum_values = True
