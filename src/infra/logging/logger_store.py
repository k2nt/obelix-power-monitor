from typing import Dict

import logging
import logging.config

from . import formatter
from .types import LogLevel, Logger


_LOGGERS: Dict[str, Logger] = {}


def get_logger(name: str = 'default'):
    """Get an existing logger
    
    Args:
        name -- str: Logger name [default: 'default']
        
    Raises:
        KeyError: If cannot find logger with given name
        
    Returns:
        src.infra.logging.types.Logger: Logger
    """
    if name not in _LOGGERS.keys():
        raise KeyError(f"logger {name} not found")
    return _LOGGERS[name]


def new_logger(
        name: str = 'default',
        level: LogLevel = LogLevel.INFO,
        fmt: formatter.Formatter = formatter.Default()
) -> Logger:    
    """Create a new logger
    
    Args:
        name -- str: Logger name [default: 'default']
        level -- src.infra.logging.LogLevel: Log level [default: LogLevel.INFO]
        fmt -- src.infra.logging.types.Formatter: Custom formatter [default: src.infra.logging.formatter.Default()]
        
    Raises:
        KeyError: If logger with given name already exists
        
    Returns:
        src.infra.logging.types.Logger: Logger
    """
    if name in _LOGGERS.keys():
        raise KeyError(f"logger {name} already exists, use 'get_logger' instead")
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    ch = logging.StreamHandler()
    ch.setLevel(level)

    ch.setFormatter(fmt)
    
    logger.addHandler(ch)
    
    # register new logger
    _LOGGERS[name] = logger
    
    return logger
