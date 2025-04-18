from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from Domain.Entities.Activities import Activities


class Components(SQLModel, table=True):
    __tablename__ = "componentes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    subcomponente: str

    actividades: List["Activities"] = Relationship(back_populates="component")
