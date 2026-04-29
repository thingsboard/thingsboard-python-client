#
# Copyright © 2026-2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
_RetryingRESTClient — wraps RESTClientObject with HTTP 429 retry logic.

Mirrors Java client's RetryingHttpClient.java:
  - Retries only on HTTP 429 (Too Many Requests)
  - Exponential backoff: initialDelayMs * 2^(attempt-1), capped at maxDelayMs
  - +/-20% jitter applied to each computed delay
  - Retry-After response header (integer seconds) respected, capped at maxDelayMs
  - After exhausting retries, returns the last 429 response (no exception raised)
  - Drains response body before each retry to avoid connection pool exhaustion
"""

import logging
import random
import time

from .rest import RESTClientObject

logger = logging.getLogger(__name__)


class _RetryingRESTClient(RESTClientObject):
    """RESTClientObject subclass that transparently retries HTTP 429 responses."""

    def __init__(
        self, configuration, max_retries: int, initial_delay_ms: int, max_delay_ms: int
    ) -> None:
        """
        Initialise the retrying REST client.

        :param configuration: Generated Configuration object (passed to parent).
        :param max_retries: Maximum number of retry attempts after initial request.
        :param initial_delay_ms: Base delay for attempt 1 (milliseconds).
        :param max_delay_ms: Upper cap on any computed delay (milliseconds).
        """
        super().__init__(configuration)
        self._max_retries = max_retries
        self._initial_delay_ms = initial_delay_ms
        self._max_delay_ms = max_delay_ms

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def request(
        self, method, url, headers=None, body=None, post_params=None, _request_timeout=None
    ):
        """Make an HTTP request, retrying up to max_retries times on 429.

        All arguments are forwarded verbatim to RESTClientObject.request().
        On a non-429 response the response is returned immediately.
        On 429 the connection is drained, a backoff delay is applied, and the
        request is retried.  After exhausting retries the last 429 response is
        returned — callers are responsible for inspecting the status code.
        """
        response = super().request(
            method,
            url,
            headers=headers,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )

        for attempt in range(1, self._max_retries + 1):
            if response.status != 429:
                return response

            # Drain the response body to release the connection back to the pool.
            response.read()

            delay_ms = self._compute_delay(response, attempt)
            delay_s = delay_ms / 1000.0
            logger.warning(
                "HTTP 429 received (attempt %d/%d); retrying in %.2f s",
                attempt,
                self._max_retries,
                delay_s,
            )
            time.sleep(delay_s)

            response = super().request(
                method,
                url,
                headers=headers,
                body=body,
                post_params=post_params,
                _request_timeout=_request_timeout,
            )

        # Return whatever we have — could still be 429 if all retries exhausted.
        return response

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _compute_delay(self, response, attempt: int) -> int:
        """Compute the retry delay in milliseconds for the given attempt.

        Priority:
        1. Retry-After header (integer seconds) — converted to ms, capped at max.
        2. Exponential backoff: initialDelayMs * 2^(attempt-1), capped at max.
        In both cases +/-20% jitter is applied only to the exponential path;
        the Retry-After value is used as-is (after capping) per the Java reference.

        :param response: The 429 response object (used to read headers).
        :param attempt: Current attempt index, starting at 1.
        :returns: Delay in milliseconds (integer).
        """
        retry_after = response.headers.get("Retry-After")
        if retry_after is not None:
            try:
                delay_ms = int(retry_after) * 1000
                return min(delay_ms, self._max_delay_ms)
            except (ValueError, TypeError):
                pass  # Fall through to exponential backoff

        # Exponential backoff with +/-20% jitter
        base_ms = self._initial_delay_ms * (2 ** (attempt - 1))
        base_ms = min(base_ms, self._max_delay_ms)
        jitter = (random.random() * 0.4) - 0.2  # range [-0.2, +0.2)
        delay_ms = int(base_ms * (1.0 + jitter))
        # Re-apply cap: positive jitter on a maxed-out base could exceed max_delay_ms.
        return min(delay_ms, self._max_delay_ms)
