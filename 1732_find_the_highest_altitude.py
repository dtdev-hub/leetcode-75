"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

from typing import List


class Solution:
    def largest_altitude(self, gain: List[int]) -> int:
        """
        Calculate the highest altitude reached during the trip.

        Args:
            gain (List[int]): List of net gains in altitude between points.

        Returns:
            int: The highest altitude reached.
        """
        current_altitude = 0
        max_altitude = 0
        for net_gain in gain:
            current_altitude += net_gain
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude


def run_tests() -> None:
    solution = Solution()
    # Test case 1: Mixed gains and losses
    assert solution.largest_altitude([-5, 1, 5, 0, -7]) == 1, "Test case 1 failed"
    # Test case 2: All negative and positive gains
    assert solution.largest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0, "Test case 2 failed"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
