from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from Domain.Entities.Evidences import Evidences
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
    producto: str = Field(default=None)
    indicador_producto: str = Field(default=None)
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
    procesos: str

    evidencias: list["Evidences"] = Relationship(
        back_populates="actividad", sa_relationship_kwargs={"cascade": "all, delete"}
    )
    plan: Optional["ActionPlan"] = Relationship(back_populates="actividades")  # type: ignore
    subcomponente: Optional["Subcomponents"] = Relationship(back_populates="actividades")  # type: ignore
