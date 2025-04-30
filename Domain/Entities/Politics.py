from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from typing import List
from Domain.Entities.Components import Components
from Domain.Entities.ActionPlan import ActionPlan


class Politics(SQLModel, table=True):
    __tablename__ = "politicas"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    componentes: List["Components"] = Relationship(back_populates="politica")
    planes: List["ActionPlan"] = Relationship(back_populates="politica")
