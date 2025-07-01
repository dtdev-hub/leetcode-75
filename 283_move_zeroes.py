"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        id_to_remove = list()
        for i, n in enumerate(nums):
            if n == 0:
                id_to_remove.append(i)

        for i in reversed(id_to_remove):
            nums.pop(i)
            nums.append(0)

        print("nums: ", nums)

    def moveZeroes_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two-pointer approach
        left = 0  # Points to the position where next non-zero should go

        # Move all non-zero elements to the front
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        # Fill the rest with zeros
        while left < len(nums):
            nums[left] = 0
            left += 1
