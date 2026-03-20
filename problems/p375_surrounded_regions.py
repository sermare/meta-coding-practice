DESCRIPTION = """
Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'. A region is captured by flipping all
'O's into 'X's in that surrounded region.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

Examples:
  Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
  Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

  Input: board = [["X"]]
  Output: [["X"]]
"""

def solution(board):
    """
    Capture all surrounded regions. Returns the modified board.

    Args:
        board: List[List[str]], the board with 'X' and 'O'.

    Returns:
        List[List[str]], the board after capturing.
    """
    return None
