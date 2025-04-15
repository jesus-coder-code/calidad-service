from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from Domain.Entities.Activities import Activities

# Usamos __future__.annotations para evitar problemas con referencias adelantadas


class ActionPlan(SQLModel, table=True):
    __tablename__ = "plan_de_accion"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    vigencia: int
    actividades: List["Activities"] = Relationship(back_populates="plan")
