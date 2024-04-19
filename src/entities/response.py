from typing import Any, Dict

from pydantic import BaseModel


class Base(BaseModel):
    """Base response schema."""
    message: str
    data: Dict[str, Any] = {}
