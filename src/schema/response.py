from typing import Any, Dict, Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Base response schema."""
    message: Optional[str] = None
    data: Optional[Any] = None
