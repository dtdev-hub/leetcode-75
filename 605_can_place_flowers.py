"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        return n <= 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.canPlaceFlowers([0], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) is True
    assert solution.canPlaceFlowers([0, 0, 1, 0, 1], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) is True
    assert solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1) is False

    print("All tests passed.")
