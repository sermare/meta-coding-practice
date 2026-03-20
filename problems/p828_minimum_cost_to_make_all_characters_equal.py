DESCRIPTION = """Minimum Cost to Make All Characters Equal

You are given a 0-indexed binary string s of length n. You can apply two types
of operations on the string any number of times:
- Choose index i and flip all characters from index 0 to index i (cost: i + 1).
- Choose index i and flip all characters from index i to index n - 1 (cost: n - i).

Return the minimum cost to make all characters of the string equal.

Example:
    Input: s = "0011"
    Output: 2
    Explanation: Apply operation 2 at i=2 -> "0000". Cost = 4 - 2 = 2.

"""


def solution(s):
    return None
