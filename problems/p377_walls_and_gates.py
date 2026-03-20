DESCRIPTION = """
Walls and Gates

You are given an m x n grid rooms initialized with these three possible values:
- -1 : A wall or an obstacle.
- 0  : A gate.
- INF (2147483647) : An empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, leave it as INF.

Constraints:
- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is -1, 0, or 2147483647.

Examples:
  Input: rooms = [[2147483647,-1,0,2147483647],
                   [2147483647,2147483647,2147483647,-1],
                   [2147483647,-1,2147483647,-1],
                   [0,-1,2147483647,2147483647]]
  Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""

def solution(rooms):
    """
    Fill empty rooms with distance to nearest gate.

    Args:
        rooms: List[List[int]], the grid.

    Returns:
        List[List[int]], the grid with distances filled in.
    """
    return None
