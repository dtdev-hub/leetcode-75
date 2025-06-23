from typing import List

"""
De bai: tinh chi so truc (pivot index)
Chi so truc la chi-so index ma
tong tat ca cac so nam ben trai chi-so do = tong tat ca cac so nam ben phai chi-so do.
Hay tim chi so truc dau tien tu trai sang.
"""
nums = [1, 7, 3, 6, 5, 6]
print(nums)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        found_flag = False

        list_sum = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            left_sum = left_sum + n

            if (left_sum - n) == (list_sum - n) / 2:
                found_flag = True
                return i

        if not found_flag:
            return -1


# Test
solution = Solution()
print(solution.pivotIndex(nums))
