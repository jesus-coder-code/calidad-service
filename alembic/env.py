from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel

import os
import sys

# Añadir la raíz del proyecto al path para que se pueda importar el código del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa todos tus modelos para que Alembic los detecte
from Domain.Entities import (
    ActionPlan,
    Activities,
    Politics,
    Components,
    Subcomponents,
    Responsible,
    Term,
)

# Importa settings desde tu módulo de configuración
from Infrastructure.utils.configuration import *

# settings = Settings()
# Carga el archivo alembic.ini
config = context.config

# Establece la URL de la base de datos desde
SYNC_DATABASE_URL = DATABASE_URL.replace("postgresql+asyncpg", "postgresql")
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

# Configuración del logging
fileConfig(config.config_file_name)

# Usa SQLModel.metadata como metadata base para detectar cambios
target_metadata = SQLModel.metadata


def run_migrations_offline():
    """Ejecuta las migraciones en modo offline (sin conexión a la base de datos)"""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecuta las migraciones en modo online (requiere conexión a la base de datos)"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Ejecutar migraciones según el modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
