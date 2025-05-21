from typing import List, Optional
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlmodel import SQLModel, Field, Relationship

from Domain.Entities.Politics import Politics
from Domain.Entities.Responsible import Responsible


class Dependencies(SQLModel, table=True):
    __tablename__ = "dependencias"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)

    politicas: List["Politics"] = Relationship(back_populates="dependencia")
    responsable: Optional["Responsible"] = Relationship(
        back_populates="dependencia", sa_relationship_kwargs={"uselist": False}
    )
