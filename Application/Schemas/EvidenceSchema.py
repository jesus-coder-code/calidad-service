from typing import Optional
from pydantic import BaseModel


class EvidenceSchemaResponse(BaseModel):
    id: Optional[int]
    nombre_archivo: str
    url_archivo: str
    avances: int
    actividad_id: int

    class Config:
        from_attributes = True
