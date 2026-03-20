DESCRIPTION = """
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Examples:
  Input: target = 7, nums = [2,3,1,2,4,3]
  Output: 2
  Explanation: The subarray [4,3] has the minimal length.

  Input: target = 4, nums = [1,4,4]
  Output: 1

  Input: target = 11, nums = [1,1,1,1,1,1,1,1]
  Output: 0
"""


def solution(target, nums):
    """
    Find the minimal length of a subarray with sum >= target.

    Args:
        target: int - the target sum
        nums: List[int] - array of positive integers

    Returns:
        int - minimal subarray length, or 0 if no such subarray exists
    """
    return None
