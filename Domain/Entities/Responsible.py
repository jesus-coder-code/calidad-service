from typing import Optional, List
from sqlmodel import SQLModel, Relationship, Field
from pydantic import EmailStr
from sqlalchemy import BigInteger, Column, ForeignKey, Integer

from Domain.Enums.RolEnum import RolEnum


class Responsible(SQLModel, table=True):
    __tablename__ = "responsables"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: EmailStr
    telefono: int = Field(sa_column=Column(BigInteger))
    rol: RolEnum = Field(default=RolEnum.LIDER)
    dependencia_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("dependencias.id", ondelete="SET NULL")),
    )

    dependencia: Optional["Dependencies"] = Relationship(back_populates="responsable")  # type: ignore
    politicas: List["Politics"] = Relationship(back_populates="responsable")  # type: ignore
