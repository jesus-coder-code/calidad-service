from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from sqlalchemy import BigInteger, Column

from Domain.Enums.RolEnum import RolEnum


class Responsible(SQLModel, table=True):
    __tablename__ = "responsables"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: EmailStr
    telefono: int = Field(sa_column=Column(BigInteger))
    rol: RolEnum = Field(default=RolEnum.LIDER)
