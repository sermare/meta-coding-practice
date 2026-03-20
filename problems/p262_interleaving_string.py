DESCRIPTION = """Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m substrings respectively, such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200

Example:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: True
"""


def solution(s1, s2, s3):
    return None
