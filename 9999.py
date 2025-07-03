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
        max_avg = float('-inf')
        i = 0
        temp_sum = 0

        while i + k <= len(nums):

            if i == 0:
                for j in range(i, i + k):
                    temp_sum += nums[j]
            else:
                temp_sum = temp_sum - nums[i - 1] + nums[i + k - 1]

            avg = temp_sum / k
            if avg > max_avg:
                max_avg = avg

            i += 1

        return max_avg


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert abs(solution.findMaxAverage(
        [1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-5
    assert abs(solution.findMaxAverage([5], 1) - 5.0) < 1e-5

    print("All tests passed.")
