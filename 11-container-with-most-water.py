"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            max_area = max(max_area, area)

            # Move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.maxArea([3, 6, 1]) == 3
    assert solution.maxArea([8, 7, 2, 1]) == 7
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1

    print("All tests passed.")
