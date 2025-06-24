"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]

    print("All tests passed.")