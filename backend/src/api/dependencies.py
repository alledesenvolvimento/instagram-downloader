from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.connection import obter_sessao


async def get_db(
    sessao: AsyncSession = Depends(obter_sessao),
) -> AsyncGenerator[AsyncSession, None]:
    """Dependency que fornece a sessão do banco para os endpoints."""
    yield sessao