from dataclasses import dataclass

import logging


@dataclass(init=True, frozen=True)
class LogLevel:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    

Logger = logging.Logger
Formatter = logging.Formatter    
