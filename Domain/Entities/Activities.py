from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from Domain.Enums.CicloEnum import CicloEnum
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer

# Usamos __future__.annotations para evitar problemas con referencias adelantadas


class Activities(SQLModel, table=True):
    __tablename__ = "actividades"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    ciclo: CicloEnum = Field(default=CicloEnum.PLANEAR)
    plan_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("plan_de_accion.id", ondelete="SET NULL")),
    )
    subcomponent_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("subcomponentes.id", ondelete="SET NULL")),
    )

    plan: Optional["ActionPlan"] = Relationship(back_populates="actividades")  # type: ignore
    subcomponente: Optional["Subcomponents"] = Relationship(back_populates="actividades")  # type: ignore
