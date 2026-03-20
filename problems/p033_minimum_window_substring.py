DESCRIPTION = """
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Examples:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from
string t.

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest
window of s only has one 'a', return empty string.
"""


def solution(s: str, t: str) -> str:
    """
    Find the minimum window in s containing all characters of t.

    Args:
        s: The source string to search within.
        t: The target string whose characters must all be present.

    Returns:
        The minimum window substring, or "" if no valid window exists.
    """
    return None
