from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from Application.Schemas.EvidenceSchema import EvidenceSchemaResponse
from Domain.Enums.CicloEnum import CicloEnum


class ActivityRequest(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum
    producto: str
    indicador_producto: str
    plan_id: int
    subcomponent_id: int

    class Config:
        from_attributes = True
        use_enum_values = True


class ActivityResponse(BaseModel):
    id: Optional[int]
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum
    producto: str
    indicador_producto: str
    plan_id: Optional[int]
    subcomponent_id: Optional[int]
    evidencias: List[EvidenceSchemaResponse] = []

    class Config:
        from_attributes = True
        use_enum_values = True


class ActivityBaseResponse(BaseModel):
    id: Optional[int]
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum
    producto: str
    indicador_producto: str
    plan_id: Optional[int]
    subcomponent_id: Optional[int]

    class Config:
        from_attributes = True
        use_enum_values = True
