from typing import Optional, List
from pydantic import BaseModel, EmailStr
from Application.Schemas.PoliticSchema import PoliticSchemaBaseResponse
from Domain.Enums.RolEnum import RolEnum


class ResponsibleSchemaRequest(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: int
    rol: RolEnum
    dependencia_id: Optional[int]

    class Config:
        from_attributes = True
        use_enum_values = True


class ResponsibleSchemaResponse(BaseModel):
    id: Optional[int]
    nombre: str
    correo: EmailStr
    telefono: int
    rol: RolEnum
    dependencia_id: Optional[int]

    class Config:
        from_attributes = True
        use_enum_values = True


class ResponsibleWithPolitic(BaseModel):
    id: Optional[int]
    nombre: str
    correo: EmailStr
    telefono: int
    rol: RolEnum
    dependencia_id: Optional[int]
    politicas: List[PoliticSchemaBaseResponse]

    class Config:
        from_attributes = True
        use_enum_values = True


class ResponsibleBasicResponse(BaseModel):
    id: Optional[int]
    nombre: str

    class Config:
        from_attributes = True
