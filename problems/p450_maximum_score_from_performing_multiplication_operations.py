DESCRIPTION = """Maximum Score from Performing Multiplication Operations

You are given two integer arrays `nums` and `multipliers` of size n and m respectively,
where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the i-th
operation (0-indexed), you will:
- Choose one integer x from either the start or the end of the array nums.
- Add multipliers[i] * x to your score.
- Remove x from the array nums.

Return the maximum score after performing m operations.

Example:
    Input: nums = [1,2,3], multipliers = [3,2,1]
    Output: 14
    Explanation: An optimal solution: pick 3 (end), pick 2 (end), pick 1 (start).
    Score = 3*3 + 2*2 + 1*1 = 14.
"""


def solution(nums, multipliers):
    return None
