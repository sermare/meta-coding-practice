DESCRIPTION = """
Custom Sort String

You are given two strings, `order` and `s`. All characters of `order` are unique
and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted.
More specifically, if a character x occurs before a character y in `order`, then x
should occur before y in the permuted string.

Return any permutation of `s` that satisfies this property.

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All characters of order are unique.

Examples:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "c", "b", "a" appear in order, so the order of "c", "b", "a" is
"c" before "b" before "a". Since "d" does not appear in order, it can be at any
position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Input: order = "bcafg", s = "abcd"
Output: "bcad"

Note: Characters not in order can be placed in any position.
"""


def solution(order: str, s: str) -> str:
    """
    Sort string s such that characters appear in the order defined by the order string.

    Args:
        order: A string defining the custom character ordering.
        s: The string to be sorted.

    Returns:
        A permutation of s sorted according to the custom order.
    """
    return None
