from pydantic import BaseModel
from datetime import date


class ActivitySchema(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    plan_id: int

    class Config:
        from_attributes = True
