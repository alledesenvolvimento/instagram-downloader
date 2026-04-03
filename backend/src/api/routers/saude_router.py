from fastapi import APIRouter


router = APIRouter(prefix="/saude", tags=["Saúde"])


@router.get("", summary="Health check")
async def verificar_saude() -> dict:
    """Verifica se a API está respondendo corretamente."""
    return {"status": "ok", "mensagem": "Instagram Downloader API está no ar! 🚀"}