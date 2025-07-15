"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import List
from collections import Counter


class Solution:
    def maxOperations_Counter_1(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum number of operations where each operation consists of removing two numbers whose sum is k.
        """
        count = 0
        freq = Counter(nums)
        for num in list(freq.keys()):
            complement = k - num
            if complement in freq:
                if num == complement:
                    pairs = freq[num] // 2
                else:
                    pairs = min(freq[num], freq[complement])
                count += pairs
                freq[num] -= pairs
                freq[complement] -= pairs
        return count

    def maxOperations_Counter_2(self, nums: List[int], k: int) -> int:
        """
        Approach 1: Using Counter (Hash Map)
        Time: O(n), Space: O(n)
        """
        count = Counter(nums)
        operations = 0

        for num in count:
            complement = k - num

            if num == complement:
                # Special case: num + num = k
                operations += count[num] // 2
            elif num < complement and complement in count:
                # Normal case: avoid double counting by only processing when num < complement
                operations += min(count[num], count[complement])

        return operations

    def maxOperations_twoPointers(self, nums: List[int], k: int) -> int:
        """
        Approach 2: Two Pointers after sorting
        Time: O(n log n), Space: O(1)
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operations


def run_tests() -> None:
    solution = Solution()

    assert (
        solution.maxOperations(
            [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3
        )
        == 4
    )
    assert solution.maxOperations([1, 1, 3, 3], 4) == 2
    assert solution.maxOperations([1, 2, 3, 4], 5) == 2
    assert solution.maxOperations([3, 1, 3, 4, 3], 6) == 1

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
