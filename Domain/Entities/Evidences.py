from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer


class Evidences(SQLModel, table=True):
    __tablename__ = "evidencias"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_archivo: str
    url_archivo: str
    avances: float
    created_at: date
    actividad_id: int = Field(
        sa_column=Column(Integer, ForeignKey("actividades.id", ondelete="CASCADE"))
    )

    actividad: Optional["Activities"] = Relationship(back_populates="evidencias")  # type: ignore
