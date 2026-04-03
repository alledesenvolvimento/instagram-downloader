import asyncio
import uvicorn
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.exception_handlers import registrar_handlers
from src.api.router import router_principal
from src.config.settings import configuracoes


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Gerencia o ciclo de vida da aplicação.
    O que está antes do yield roda no startup.
    O que está depois do yield roda no shutdown.
    """
    print("🚀 Instagram Downloader API iniciando...")
    print(f"   Ambiente: {configuracoes.environment}")
    print(f"   Porta: {configuracoes.port}")
    yield
    print("👋 Instagram Downloader API encerrando...")


def criar_app() -> FastAPI:
    """
    Factory function que cria e configura a aplicação FastAPI.
    Usar uma factory facilita testes e múltiplas instâncias.
    """
    app = FastAPI(
        title="Instagram Downloader API",
        description="API para download automatizado de conteúdos públicos do Instagram.",
        version="0.1.0",
        docs_url="/docs" if configuracoes.environment == "development" else None,
        redoc_url=None,
        lifespan=lifespan,
    )

    # CORS — liberado em desenvolvimento
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rotas
    app.include_router(router_principal)

    # Exception handlers
    registrar_handlers(app)

    return app


app = criar_app()


if __name__ == "__main__":
    uvicorn.run(
        "src.server:app",
        host="0.0.0.0",
        port=configuracoes.port,
        reload=configuracoes.environment == "development",
    )