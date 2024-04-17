from fastapi import APIRouter

from .monitor import router as monitor_router


router = APIRouter(prefix='/api/v1')

router.include_router(monitor_router)
