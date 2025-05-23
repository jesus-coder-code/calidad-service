from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from typing import List
from Domain.Entities.Components import Components
from Domain.Entities.ActionPlan import ActionPlan


class Politics(SQLModel, table=True):
    __tablename__ = "politicas"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    dependencia_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("dependencias.id", ondelete="SET NULL")),
    )
    responsable_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("responsables.id", ondelete="SET NULL")),
    )

    componentes: List["Components"] = Relationship(back_populates="politica")
    planes: List["ActionPlan"] = Relationship(back_populates="politica")
    dependencia: Optional["Dependencies"] = Relationship(back_populates="politicas")  # type: ignore
    responsable: Optional["Responsible"] = Relationship(back_populates="politicas")  # type: ignore
