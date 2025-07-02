"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, max_altitude = 0, 0
        for i, n in enumerate(gain):
            altitude += n
            if max_altitude < altitude:
                max_altitude = altitude

        return max_altitude


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0

    print("All tests passed.")
