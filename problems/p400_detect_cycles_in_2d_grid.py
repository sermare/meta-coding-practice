DESCRIPTION = """
Detect Cycles in 2D Grid

Given a 2D array of characters grid of size m x n, you need to find if there
exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the
same cell. From a given cell, you can move to one of the cells adjacent to it
(up, down, left, right) if it has the same value.

Also, you cannot move to the cell that you visited in your last move (no
immediate reversal).

Return true if any cycle of the same value exists in grid, otherwise return false.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid consists only of lowercase English letters.

Examples:
  Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
  Output: True

  Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
  Output: True

  Input: grid = [["a","b"],["b","a"]]
  Output: False
"""

def solution(grid):
    """
    Detect if there exists a cycle of the same value in the grid.

    Args:
        grid: List[List[str]], the 2D character grid.

    Returns:
        Boolean, True if a cycle exists.
    """
    return None
