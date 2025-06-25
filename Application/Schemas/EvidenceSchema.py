from typing import Optional
from pydantic import BaseModel
from datetime import date


class EvidenceSchemaResponse(BaseModel):
    id: Optional[int]
    nombre_archivo: str
    url_archivo: str
    avances: float
    created_at: date
    actividad_id: int

    class Config:
        from_attributes = True
