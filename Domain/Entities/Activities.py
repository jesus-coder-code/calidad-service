from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date

# Usamos __future__.annotations para evitar problemas con referencias adelantadas


class Activities(SQLModel, table=True):
    __tablename__ = "actividades"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    fecha_inicio: date
    fecha_final: date
    responsable: str
    meta: str
    plan_id: Optional[int] = Field(default=None, foreign_key="plan_de_accion.id")
    component_id: Optional[int] = Field(default=None, foreign_key="componentes.id")

    plan: Optional["ActionPlan"] = Relationship(back_populates="actividades")  # type: ignore
    component: Optional["Components"] = Relationship(back_populates="actividades")  # type: ignore
