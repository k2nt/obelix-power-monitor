from enum import Enum
from http import HTTPStatus  # Inherit the HTTPStatus object from the standard library


Status = HTTPStatus


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    