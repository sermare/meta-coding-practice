DESCRIPTION = """Pour Water

We are given an elevation map, `heights[i]` representing the height of the terrain
at that index. The width at each index is 1. After `V` units of water fall at index
`K`, how much water is at each index?

Water first drops at index K, and rests on top of the highest terrain or water at
that index. Then, water flows to the left preferring lower positions, then to the
right preferring lower positions. If it cannot flow anywhere, it stays at K.

Example:
    Input: heights = [2,1,1,2,1,2,2], V = 4, K = 3
    Output: [2,2,2,3,2,2,2]
    Explanation: Water fills the valleys around index K.
"""


def solution(heights, V, K):
    return None
