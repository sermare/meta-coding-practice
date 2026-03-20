DESCRIPTION = """UTF-8 Validation

Given an integer array data representing the data, return whether it is a valid
UTF-8 encoding.

A character in UTF-8 can be from 1 to 4 bytes long, subjected to the following rules:
- For a 1-byte character, the first bit is 0, followed by its Unicode code.
- For an n-bytes character, the first n bits are all ones, the n+1 bit is 0,
  followed by n-1 bytes with most significant 2 bits being 10.

Only the 8 least significant bits of each integer are used (the rest are ignored).

Example:
    Input: data = [197, 130, 1]
    Output: True
    Explanation: 197 = 11000101, 130 = 10000010, 1 = 00000001
    This is a valid 2-byte char followed by a 1-byte char.
"""


def solution(data):
    return None
