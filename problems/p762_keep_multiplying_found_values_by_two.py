DESCRIPTION = """Keep Multiplying Found Values by Two

You are given an array of integers nums. You are also given an integer original
which is the first number that needs to be searched for in nums.

You then do the following steps:
1. If original is found in nums, multiply it by two (original *= 2).
2. Otherwise, stop the process.
3. Repeat this process with the new number as long as you keep finding the number.

Return the final value of original.

Example:
    Input: nums = [5,3,6,1,12], original = 3
    Output: 24
    Explanation: 3 found -> 6, 6 found -> 12, 12 found -> 24, 24 not found.
"""


def solution(nums, original):
    return None
