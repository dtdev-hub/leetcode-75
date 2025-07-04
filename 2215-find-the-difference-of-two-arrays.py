"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        res_1 = set()
        res_2 = set()

        for n1 in set1:
            if n1 not in set2 and n1 not in res_1:
                res_1.add(n1)

        for n2 in set2:
            if n2 not in set1 and n2 not in res_2:
                res_2.add(n2)

        res = [list(res_1), list(res_2)]
        return res



# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.findDifference([1,2,3], [2,4,6]) == [[1,3],[4,6]]
    assert solution.findDifference([1,2,3,3], [1,1,2,2]) == [[3],[]]


    print("All tests passed.")
