DESCRIPTION = """String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
integer (similar to C/C++'s atoi function).

The algorithm:
1. Read in and ignore any leading whitespace.
2. Check if the next character is '-' or '+'. Read this character in if it is either.
3. Read in next the characters until the next non-digit character or the end of the
   input is reached. The rest of the string is ignored.
4. Convert these digits into an integer. If no digits were read, then the integer is 0.
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then
   clamp the integer so that it remains in the range.

Example:
    Input: s = "42"
    Output: 42

    Input: s = "   -42"
    Output: -42

    Input: s = "4193 with words"
    Output: 4193

Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


def solution(s):
    return None
