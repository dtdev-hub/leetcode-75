"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            # Expand the sliding window with nums[right]
            if nums[right] == 0:
                zero_count += 1

            # If the number of 0s exceeds k, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10

    print("All tests passed.")
