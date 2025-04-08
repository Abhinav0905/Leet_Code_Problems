# 14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Solution 
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" # Handles the edge case whern the input list is empty
        
        # Start with the first string as the prefix
        prefix = strs[0]

        # compare the prefix with each string in the list
        for string in strs[1:]:
            while not string.startswith(prefix):
                # If the prefix is not a prefix of the string, reduce the prefix
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


solution = Solution()
strs = input("Enter the list of the words: ").split(",")
output = solution.longestCommonPrefix(strs)
print(f"The {output} has common ")
