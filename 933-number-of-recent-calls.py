"""
RecentCounter tracks the number of requests received in the past 3000 milliseconds.

The original implementation used a standard list to store request timestamps and removed
expired entries with ``pop(0)``. This resulted in ``O(n)`` time complexity per operation,
which could become slow as the number of requests grew.

This version uses ``collections.deque`` to achieve ``O(1)`` removals from the left,
ensuring that the ``ping`` method runs efficiently.
"""

from collections import deque


class RecentCounter:
    """Count recent requests in the last 3000 milliseconds."""

    def __init__(self) -> None:
        # Using deque allows O(1) pops from the left as older timestamps expire
        self.requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """Record a new request and return the number within the past 3000 ms."""

        # Add the current timestamp
        self.requests.append(t)

        # Remove requests older than 3000ms
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of requests in the time window
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
