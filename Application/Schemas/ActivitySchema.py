from typing import List, Optional
from pydantic import BaseModel, computed_field, Field
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
    procesos: Optional[str] = None

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
    procesos: Optional[str]
    evidencias: List[EvidenceSchemaResponse] = []

    @computed_field
    @property
    def progreso_total(self) -> float:
        return sum(e.avances for e in self.evidencias)

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
    procesos: Optional[str]

    class Config:
        from_attributes = True
        use_enum_values = True


class ActivitySummaryResponse(ActivityResponse):
    evidencias: list = Field(exclude=True)

    @computed_field(return_type=float)
    @property
    def progreso_total(self) -> float:
        return sum(e.avances for e in self.evidencias)
