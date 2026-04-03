from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config.settings import configuracoes


engine = create_async_engine(
    configuracoes.database_url,
    echo=configuracoes.environment == "development",
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def obter_sessao() -> AsyncGenerator[AsyncSession, None]:
    """Dependency injection — fornece uma sessão de banco por requisição."""
    async with SessionLocal() as sessao:
        yield sessao