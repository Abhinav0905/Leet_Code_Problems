# Title: LeetCode 00013. Roman to Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/roman-to-integer/
# Tags: String, Math
# Description:
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

# Solution


class Solution:
    def romanToInt(self, s: str) -> int:
        index = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special_series = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        x = list(s)
        print(x)
        y = []
        i = 0
        while i < len(x):
            if i + 1 < len(x) and x[i] + x[i+1] in special_series:
                y.append(special_series[x[i] + x[i+1]])
                i += 2
                print("AAA",i)
            else:
                y.append(index[x[i]])
                i += 1
                print("BBB",i)
        return sum(y)

s = input("Enter the Roman numeral in CAPS: ").upper().strip()

allowed = set("IVXLCDM")
s = "".join([char for char in s if char in allowed])

print(f"The entered Roman numeral is {s}")
solution = Solution()
result = solution.romanToInt(s)
print(f"The output is {result}")