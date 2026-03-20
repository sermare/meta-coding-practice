DESCRIPTION = """Circular Array Loop

You are playing a game involving a circular array of non-zero integers nums. Each
nums[i] denotes the number of indices forward/backward you must move if you are
located at index i:
- If nums[i] is positive, move nums[i] steps forward.
- If nums[i] is negative, move nums[i] steps backward.

Since the array is circular, you may assume that moving forward from the last
element puts you on the first element, and moving backward from the first element
puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:
- Following the movement rules above results in a repeating index sequence.
- All nums[seq[j]] are either all positive or all negative.
- k > 1

Return true if there is a cycle in nums, or false otherwise.

Example:
    Input: nums = [2,-1,1,2,2]
    Output: True
    Explanation: Index 0 -> 2 -> 3 -> 0 (all positive, length 3).
"""


def solution(nums):
    return None
