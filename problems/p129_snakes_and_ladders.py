DESCRIPTION = """Snakes and Ladders

You are given an n x n integer matrix board where the cells are labeled from 1 to n^2
in a Boustrophedon style starting from the bottom left of the board (i.e. board[n-1][0])
and alternating direction each row.

You start on square 1. In each move, starting from square curr, you choose a destination
square next with label in the range [curr + 1, min(curr + 6, n^2)].

If next has a snake or ladder, you must move to the destination of that snake or ladder.
Otherwise, you move to next. A board square with value -1 has no snake or ladder.

Return the least number of dice rolls to reach square n^2. If it is not possible, return -1.

Example:
    Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
                    [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    Output: 4

Constraints:
- n == board.length == board[i].length
- 2 <= n <= 20
- board[i][j] is either -1 or in the range [1, n^2].
- The squares labeled 1 and n^2 do not have any snakes or ladders.
"""


def solution(board):
    return None
