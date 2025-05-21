from typing import AsyncGenerator
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from Domain.Entities import (
    Activities,
    ActionPlan,
    Components,
    Subcomponents,
    Politics,
    Responsible,
    Term,
    Dependencies,
    Evidences,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Usar create_async_engine para conexiones asíncronas
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Configuración correcta de sessionmaker
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# ✅ Función para obtener sesión
@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()


# ✅ Función para crear tablas
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
