DESCRIPTION = """Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive
formula:
- countAndSay(1) = "1"
- countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing
consecutive identical characters with the character concatenated with the count.

Example:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = "11"  (one 1)
        countAndSay(3) = "21"  (two 1s)
        countAndSay(4) = "1211" (one 2, one 1)
"""


def solution(n):
    return None
