DESCRIPTION = """
Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (0, 0) to the
bottom-right cell (n - 1, n - 1) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected.

The length of a clear path is the number of visited cells of this path.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Examples:
  Input: grid = [[0,1],[1,0]]
  Output: 2

  Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
  Output: 4

  Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
  Output: -1
"""

def solution(grid):
    """
    Return the length of the shortest clear path in the binary matrix.

    Args:
        grid: List[List[int]], the binary matrix.

    Returns:
        An integer, the shortest path length or -1.
    """
    return None
