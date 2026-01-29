from fastapi import APIRouter

from .source import source_router

router_v1 = APIRouter(prefix="/v1", tags=["v1"])
router_v1.include_router(source_router)

router = APIRouter(prefix="/api")
router.include_router(router_v1)
