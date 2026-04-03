from arq import Worker
from arq.connections import RedisSettings

from src.config.settings import configuracoes
from src.infrastructure.queue.tasks import baixar_perfil


async def startup(ctx: dict) -> None:
    """Inicializa o contexto do worker."""
    pass


async def shutdown(ctx: dict) -> None:
    """Limpa o contexto do worker."""
    pass


class WorkerSettings:
    """Configurações do worker ARQ."""

    functions = [baixar_perfil]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = RedisSettings.from_dsn(configuracoes.redis_url)
    max_jobs = 10