from typing import List, Optional
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlmodel import SQLModel, Field, Relationship
from Domain.Enums.TermEnum import TermEnum
from Domain.Entities.ActionPlan import ActionPlan


class Term(SQLModel, table=True):
    __tablename__ = "vigencias"

    id: Optional[int] = Field(default=None, primary_key=True)
    vigencia: int = Field(unique=True)
    estado: TermEnum = Field(default=TermEnum.ABIERTO)

    planes: List["ActionPlan"] = Relationship(back_populates="vigencia")
