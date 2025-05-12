from typing import List, Optional
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from Domain.Entities.Activities import Activities

# Usamos __future__.annotations para evitar problemas con referencias adelantadas


class ActionPlan(SQLModel, table=True):
    __tablename__ = "plan_de_accion"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    vigencia_id: int = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("vigencias.id", ondelete="RESTRICT")),
    )
    politica_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("politicas.id", ondelete="SET NULL")),
    )

    actividades: List["Activities"] = Relationship(back_populates="plan")
    politica: Optional["Politics"] = Relationship(back_populates="planes")  # type: ignore
    vigencia: Optional["Term"] = Relationship(back_populates="planes")  # type: ignore
