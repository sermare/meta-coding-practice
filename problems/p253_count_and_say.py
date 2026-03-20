DESCRIPTION = """Count and Say

The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from
  countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number
of substrings such that each substring contains exactly one unique digit.
Then for each substring, say the number of digits, then say the digit.
Finally, concatenate every said digit.

Example:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = "11"   (one 1)
        countAndSay(3) = "21"   (two 1s)
        countAndSay(4) = "1211" (one 2, one 1)
"""


def solution(n):
    return None
