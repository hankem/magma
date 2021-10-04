import logging
from typing import Optional

from sentry_sdk import capture_event


class Logger:
    def __init__(self, name: Optional[str] = None) -> None:
        self._logger = logging.getLogger(name)

    def debug(self, *args, **kwargs) -> None:
        self._logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs) -> None:
        self._logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs) -> None:
        self._logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs) -> None:
        self._logger.error(*args, **kwargs)

    def sentry_error(self, *args, **kwargs) -> None:
        self.error(*args, **kwargs)
        capture_event({**kwargs, "args": args})   # FIXME
