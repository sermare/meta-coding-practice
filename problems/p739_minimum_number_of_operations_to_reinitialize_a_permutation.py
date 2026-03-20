DESCRIPTION = """Minimum Number of Operations to Reinitialize a Permutation

You are given an even integer n. You have a permutation perm of size n where
perm[i] == i (0-indexed).

In one operation, you create a new array arr where:
- If i % 2 == 0, then arr[i] = perm[i / 2]
- If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2]

You then assign arr to perm.

Return the minimum non-zero number of operations you need to perform on perm to return
it to its initial value.

Example:
    Input: n = 2
    Output: 1

    Input: n = 4
    Output: 2
"""


def solution(n):
    return None
