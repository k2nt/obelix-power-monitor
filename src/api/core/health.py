"""The so-called 'z-pages' for system heath checks."""
from fastapi import APIRouter

from src.domain import response


router = APIRouter()


@router.get('/livez')
async def livez():
    """Liveness probe."""
    return response.ok_empty()


@router.get('/readyz')
async def readyz():
    """Readiness probe."""
    return response.ok_empty()
