DESCRIPTION = """
Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j]
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and
only if the elevation of both squares individually are at most t.

Return the least time until you can reach the bottom right square (n-1, n-1)
from the top left square (0, 0).

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value in grid is unique.

Examples:
  Input: grid = [[0,2],[1,3]]
  Output: 3

  Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
  Output: 16
"""

def solution(grid):
    """
    Return the least time to swim from top-left to bottom-right.

    Args:
        grid: List[List[int]], the elevation grid.

    Returns:
        An integer, the minimum time.
    """
    return None
