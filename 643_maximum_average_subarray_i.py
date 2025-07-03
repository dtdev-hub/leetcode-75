"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert abs(solution.findMaxAverage(
        [1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-5
    assert abs(solution.findMaxAverage([5], 1) - 5.0) < 1e-5

    print("All tests passed.")
