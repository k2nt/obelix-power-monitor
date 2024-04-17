import logging

from src.lib.format import strfmt
from .types import Formatter


_DEFAULT_FORMAT = "%(asctime)s  %(levelname)s  %(message)s"
_DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _color_by_log_level(s: str, level: int) -> str:
    match level:
        case logging.DEBUG:
            return strfmt.cyan(s)
        case logging.INFO:
            return strfmt.white(s)
        case logging.WARNING:
            return strfmt.yellow(s)
        case logging.ERROR:
            return strfmt.red(s)
        case logging.CRITICAL:
            return strfmt.red(s)
        case _:
            return strfmt.white(s)


class Default(Formatter):
    """Custom formatter class for API logging."""
    def __init__(
            self, 
            dfmt: str = _DEFAULT_FORMAT,
            datefmt: str = _DEFAULT_DATE_FORMAT,
    ):
        super().__init__(fmt=dfmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord):                
        return _color_by_log_level(super().format(record), record.levelno)
    
    
DEFAULT_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            '()': Default,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'formatter': 'default',
        #     'class': 'logging.FileHandler',
        #     'filename': 'logs/sinfonia.log',
        #     'mode': 'a',
        # }
    },
    'loggers': {
        'main': { 
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
} 
    