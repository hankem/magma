"""
Copyright 2021 The Magma Authors.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
