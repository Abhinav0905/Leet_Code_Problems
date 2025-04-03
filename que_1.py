# 1. Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

"""

# Solution 1
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the numbers
        num_indices = {}
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # calculate the complement of the current number
            complement = target - num
            # Check if the complement is already in the dictionary
            if complement in num_indices:
                # If found, return the indices of the two numbers
                return [num_indices[complement], i]
            # If not found, store the index of the current number in the dictionary     # NOQA E501
            num_indices[num] = i
        # If no solution is found, return an empty list
        return []

# Example usage


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(f"Indices of the two numbers that add up to {target} are: {result}")
# Output: Indices of the two numbers that add up to 9 are: [0, 1]