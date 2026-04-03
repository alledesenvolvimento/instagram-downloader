import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from src.config.settings import configuracoes
from src.infrastructure.persistence.models.base_model import ModelBase

# Lê as configurações de logging do alembic.ini
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Aponta para os metadata dos models — necessário para autogenerate
target_metadata = ModelBase.metadata


def rodar_migrations_offline() -> None:
    """Roda as migrations sem conexão com o banco (modo offline)."""
    context.configure(
        url=configuracoes.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


async def rodar_migrations_online() -> None:
    """Roda as migrations com conexão real com o banco (modo online)."""
    engine = create_async_engine(configuracoes.database_url)

    async with engine.connect() as conexao:
        await conexao.run_sync(
            lambda conn: context.configure(
                connection=conn,
                target_metadata=target_metadata,
            )
        )
        async with context.begin_transaction():
            await conexao.run_sync(lambda _: context.run_migrations())

    await engine.dispose()


if context.is_offline_mode():
    rodar_migrations_offline()
else:
    asyncio.run(rodar_migrations_online())