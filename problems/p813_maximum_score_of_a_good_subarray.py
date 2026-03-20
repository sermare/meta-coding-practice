DESCRIPTION = """Maximum Score of a Good Subarray

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j])
* (j - i + 1).

A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Example:
    Input: nums = [1,4,3,7,4,5], k = 3
    Output: 15
    Explanation: The subarray [4,3,7,4,5] has min=3 and length=5, score=15.

"""


def solution(nums, k):
    return None
