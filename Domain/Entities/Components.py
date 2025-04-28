from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from Domain.Entities.Subcomponents import Subcomponents


class Components(SQLModel, table=True):
    __tablename__ = "componentes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    subcomponentes: List["Subcomponents"] = Relationship(back_populates="component")
