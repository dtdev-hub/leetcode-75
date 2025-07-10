"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                if num > second:
                    return True

        return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.increasingTriplet([1, 5, 0, 4, 1, 3]) is True
    #  i = 2, num_i = 0;     j = 4, num_j = 1;     k = 4, num_k = 3
    assert solution.increasingTriplet([2, 0, 4, 0, 6]) is True
    assert solution.increasingTriplet([1, 2, 2]) is False
    assert solution.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert solution.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert solution.increasingTriplet([2, 1, 5, 0, 4, 6]) is True

    print("All tests passed.")
