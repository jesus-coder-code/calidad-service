from typing import Optional
from pydantic import BaseModel, EmailStr
from Domain.Enums.RolEnum import RolEnum


class ResponsibleSchemaRequest(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: int
    rol: RolEnum

    class Config:
        from_attributes = True
        use_enum_values = True


class ResponsibleSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    correo: EmailStr
    telefono: int
    rol: RolEnum

    class Config:
        from_attributes = True
        use_enum_values = True
