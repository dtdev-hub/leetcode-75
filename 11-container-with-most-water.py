"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

# area = (j-i) * min(n[i], n[j])


class Solution:
    @staticmethod
    def update_max_area(current, new):
        if current < new:
            current = new
        return current

    @staticmethod
    def calculate_area(i, h1, j, h2):
        area = (j - i) * min(h1, h2)
        return area

    def maxArea(self, height: List[int]) -> int:
        span = len(height)
        max_area = 0

        # i: 0, 0, 1           h1: 3, 3, 6
        # j: 2, 1, 1           h2: 1, 6, 6

        j = span - 1
        h2 = height[j]
        for i, h1 in enumerate(height):
            temp_area = self.calculate_area(i, h1, j, h2)
            max_area = self.update_max_area(max_area, temp_area)

            while h2 < h1 and j >= i:
                j -= 1
                h2 = height[j]
                temp_area = self.calculate_area(i, h1, j, h2)
                max_area = self.update_max_area(max_area, self.calculate_area(i, h1, j, h2))

        return max_area


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.maxArea([3, 6, 1]) == 3
    assert solution.maxArea([8, 7, 2, 1]) == 7
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1

    print("All tests passed.")
