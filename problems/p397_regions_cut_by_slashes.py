DESCRIPTION = """
Regions Cut By Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of
a '/', '\\', or blank space ' '. These characters divide the square into
contiguous regions.

Given the grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\\' is represented as '\\\\'.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 30
- grid[i][j] is either '/', '\\', or ' '.

Examples:
  Input: grid = [" /","/ "]
  Output: 2

  Input: grid = [" /","  "]
  Output: 1

  Input: grid = ["/\\","\\/"]]
  Output: 4
"""

def solution(grid):
    """
    Return the number of regions in the grid cut by slashes.

    Args:
        grid: List[str], the grid with slashes.

    Returns:
        An integer, the number of regions.
    """
    return None
