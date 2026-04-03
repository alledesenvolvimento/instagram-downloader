from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.base import ErroDeNegocio, RecursoNaoEncontrado, RequisicaoInvalida


def registrar_handlers(app: FastAPI) -> None:
    """Registra todos os exception handlers na aplicação."""

    @app.exception_handler(RecursoNaoEncontrado)
    async def handler_nao_encontrado(
        request: Request, exc: RecursoNaoEncontrado
    ) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detalhe": exc.mensagem})

    @app.exception_handler(RequisicaoInvalida)
    async def handler_requisicao_invalida(
        request: Request, exc: RequisicaoInvalida
    ) -> JSONResponse:
        return JSONResponse(status_code=400, content={"detalhe": exc.mensagem})

    @app.exception_handler(ErroDeNegocio)
    async def handler_erro_negocio(
        request: Request, exc: ErroDeNegocio
    ) -> JSONResponse:
        return JSONResponse(status_code=422, content={"detalhe": exc.mensagem})