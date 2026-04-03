from fastapi import APIRouter

from src.api.routers.saude_router import router as saude_router


router_principal = APIRouter(prefix="/api/v1")

router_principal.include_router(saude_router)