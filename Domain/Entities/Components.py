from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from Domain.Entities.Subcomponents import Subcomponents
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer


class Components(SQLModel, table=True):
    __tablename__ = "componentes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    politica_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("politicas.id", ondelete="SET NULL")),
    )

    politica: Optional["Politics"] = Relationship(back_populates="componentes")  # type: ignore
    subcomponentes: List["Subcomponents"] = Relationship(back_populates="componente")
