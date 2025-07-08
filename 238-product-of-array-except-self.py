"""238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        right_products = [1] * n
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        res = [1] * n
        for i in range(n):
            res[i] = left_products[i] * right_products[i]

        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    print("All tests passed.")
