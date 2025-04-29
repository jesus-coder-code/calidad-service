from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer


class Subcomponents(SQLModel, table=True):
    __tablename__ = "subcomponentes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    component_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("componentes.id", ondelete="SET NULL")),
    )

    actividades: List["Activities"] = Relationship(back_populates="subcomponente")  # type: ignore
    componente: Optional["Components"] = Relationship(back_populates="subcomponentes")  # type: ignore
