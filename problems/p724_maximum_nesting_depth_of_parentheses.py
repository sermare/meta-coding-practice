DESCRIPTION = """Maximum Nesting Depth of Parentheses

A string is a valid parentheses string (VPS) if it meets one of the following:
- It is an empty string "", or a single character not equal to "(" or ")",
- It can be written as AB (A concatenated with B), where A and B are VPS's, or
- It can be written as (A), where A is a VPS.

The nesting depth of a VPS is defined as the maximum number of nested parentheses.

Given a VPS represented as string s, return the nesting depth of s.

Example:
    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3
"""


def solution(s):
    return None
