import logging

from src.lib import format


_DEFAULT_FORMAT = "%(asctime)s  %(levelname)s  %(message)s"
_DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


Formatter = logging.Formatter


def _color_by_log_level(s: str, level: int) -> str:
    match level:
        case logging.DEBUG:
            return format.str.cyan(s)
        case logging.INFO:
            return format.str.white(s)
        case logging.WARNING:
            return format.str.yellow(s)
        case logging.ERROR:
            return format.str.red(s)
        case logging.CRITICAL:
            return format.str.red(s)
        case _:
            return format.str.white(s)


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