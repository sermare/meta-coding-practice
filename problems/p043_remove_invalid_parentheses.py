DESCRIPTION = """
Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum
number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of
removals. You may return the answer in any order.

Constraints:
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'
- There will be at most 20 parentheses in s

Examples:
  Input: s = "()())()"
  Output: ["(())()","()()()"]

  Input: s = "(a)())()"
  Output: ["(a())()","(a)()()"]

  Input: s = ")("
  Output: [""]
"""


def solution(s):
    """
    Remove the minimum number of invalid parentheses to make the string valid.

    Args:
        s: str - a string containing letters and parentheses

    Returns:
        List[str] - all possible valid strings with minimum removals
    """
    return None
