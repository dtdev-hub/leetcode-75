"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_order = defaultdict(list)
        nums_set = set(nums)
        for i, n in enumerate(nums):
            num_order[n].append(i)

        indices_to_remove = list()
        count = 0
        # edge cases
        if len(nums) == 1:
            return 0

        # normal cases
        for i1, n1 in enumerate(nums):
            n2 = k - n1
            if (n1 == n2 and len(num_order[n2]) > 1) or (
                n1 != n2
                and n2 in nums_set
                and len(num_order[n1]) > 0
                and len(num_order[n2]) > 0
            ):
                print("n1, n2: ", n1, n2)
                print("num_order begin: ", num_order)
                count += 1
                indices_to_remove.append(i1)
                # i2
                i2 = num_order[n2][-1]
                indices_to_remove.append(i2)

                num_order[n1].pop(0)
                num_order[n2].pop(-1)
                print("num_order end: ", num_order)

        return count


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
