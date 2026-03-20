DESCRIPTION = """
Problem 11: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Examples:
  Input: nums = [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]
  Explanation: The distinct triplets are [-1, -1, 2] and [-1, 0, 1].

  Input: nums = [0, 1, 1]
  Output: []
  Explanation: The only possible triplet does not sum up to 0.

  Input: nums = [0, 0, 0]
  Output: [[0, 0, 0]]
  Explanation: The only possible triplet sums up to 0.
"""


def solution(nums):
    """
    Find all unique triplets in the array that sum to zero.

    Args:
        nums: List of integers.

    Returns:
        A list of lists, where each inner list is a triplet that sums to zero.
    """
    return None
