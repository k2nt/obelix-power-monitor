from dataclasses import dataclass

import logging
import logging.config
from logging import Logger

from . import formatter


@dataclass(init=True, frozen=True)
class LogLevel:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR


def get(
        name: str = 'default',
        level: LogLevel = LogLevel.INFO,
        fmt: formatter.Formatter = formatter.Default()
) -> Logger:    
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # add formatter
    ch.setFormatter(fmt)
    
    # add console handler to logger
    logger.addHandler(ch)
    
    return logger
