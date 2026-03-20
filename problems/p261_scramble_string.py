DESCRIPTION = """Scramble String

We can scramble a string s to get a string t using the following algorithm:
1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
   - Split the string into two non-empty substrings at a random index.
   - Randomly decide to swap the two substrings or keep them in the same order.
   - Apply step 1 recursively on each of the two substrings.

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled
string of s1, otherwise return false.

Constraints:
- s1.length == s2.length
- 1 <= s1.length <= 30
- s1 and s2 consist of lowercase English letters

Example:
    Input: s1 = "great", s2 = "rgeat"
    Output: True

    Input: s1 = "abcde", s2 = "caebd"
    Output: False
"""


def solution(s1, s2):
    return None
