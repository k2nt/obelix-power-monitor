from typing import Any, Dict, Optional

from fastapi import Response

from src.lib.http import HTTPStatus
from src.schema.response import ResponseBase


def ok(
        message: str = 'success',
        data: Dict[str, Any] = {},
) -> Response:
    """OK response builder.
    
    Args:
        message -- str: Response message [default: 'success']
        data -- Any: Data [default: None]
    
    Returns:
        fastapi.Response: Response object
    """
    resp_dict = ResponseBase(message=message, data=data).model_dump()
    return Response(
        content=str(resp_dict),
        status_code=HTTPStatus.OK,
        )


def ok_empty() -> Response:
    return Response(status_code=HTTPStatus.OK)
