DESCRIPTION = """String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
integer.

The algorithm:
1. Read in and ignore any leading whitespace.
2. Check if the next character is '-' or '+'. Read this character in if it is either.
3. Read in next characters until the next non-digit character or end of input. These
   define the number.
4. Convert these digits into an integer. If no digits were read, then the integer is 0.
5. Clamp the integer to the 32-bit signed integer range [-2^31, 2^31 - 1].

Example:
    Input: s = "42"
    Output: 42

    Input: s = "   -42"
    Output: -42

    Input: s = "4193 with words"
    Output: 4193

    Input: s = "words and 987"
    Output: 0
"""


def solution(s):
    return None
