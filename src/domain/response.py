from typing import Any, Dict

from fastapi import Response
from fastapi.responses import JSONResponse

from src.lib import http as http_lib
from src.model import response as response_model


def ok(
        message: str = 'success',
        data: Dict[str, Any] = {},
) -> JSONResponse:
    """OK response builder.
    
    Args:
        message -- str: Response message [default: 'success']
        data -- Any: Data [default: None]
    
    Returns:
        fastapi.Response: Response object
    """
    resp_dict = response_model.Base(message=message, data=data).model_dump()
    return JSONResponse(
        content=str(resp_dict),
        status_code=http_lib.Status.OK,
        )


def ok_empty() -> Response:
    return Response(status_code=http_lib.Status.OK)
