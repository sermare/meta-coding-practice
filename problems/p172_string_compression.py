DESCRIPTION = """String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters:
- If the group length is 1, append the character.
- Otherwise, append the character followed by the group's length.

Return the new length of the array after compression.

Example:
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: 6  (chars becomes ["a","2","b","2","c","3"])

    Input: chars = ["a"]
    Output: 1

    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: 4  (chars becomes ["a","b","1","2"])
"""


def solution(chars):
    return None
