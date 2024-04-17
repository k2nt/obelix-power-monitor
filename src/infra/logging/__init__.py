from .types import Level
from . import logger_store
from . import formatter
from . import types


# Create the default logger
_ = logger_store.new_logger()
