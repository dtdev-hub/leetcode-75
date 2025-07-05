"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        number_occurences = defaultdict(int)
        for n in arr:
            number_occurences[n] += 1

        occ = set()
        for v in number_occurences.values():
            if v in occ:
                return False
            else:
                occ.add(v)

        return True


# Test Case
if __name__ == "__main__":
    solution = Solution()

    assert solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
    assert solution.uniqueOccurrences([1, 2]) is False
    assert solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True

    print("All test passed.")
