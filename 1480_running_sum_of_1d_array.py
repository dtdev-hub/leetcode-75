"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = list()
        sum = 0
        for num in nums:
            sum += num
            new_list.append(sum)

        return new_list

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.runningSum([1,2,3,4]) == [1,3,6,10]
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17]

    print("All tests passed.")