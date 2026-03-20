DESCRIPTION = """Reduction Operations to Make the Array Elements Equal

Given an integer array nums, your goal is to make all elements in nums equal. To
complete one operation, follow these steps:

1. Find the largest value in nums. Let its index be i (0-indexed) and its value be
   largest. If there are multiple elements with the largest value, pick the smallest i.
2. Find the next largest value in nums strictly smaller than largest. Let its value be
   nextLargest.
3. Reduce nums[i] to nextLargest.

Return the number of operations to make all elements in nums equal.

Example:
    Input: nums = [5, 1, 3]
    Output: 3
    Explanation: [5,1,3] -> [3,1,3] -> [1,1,3] -> [1,1,1]. 3 operations.
"""


def solution(nums):
    return None
