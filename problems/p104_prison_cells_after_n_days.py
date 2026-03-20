DESCRIPTION = """Prison Cells After N Days

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether a cell is occupied or vacant changes according to the following rules:
- If a cell has two adjacent neighbors that are both occupied or both vacant, then the
  cell becomes occupied.
- Otherwise, it becomes vacant.

Note that because the prison is a row, the first and the last cells in the row can't
have two adjacent neighbors.

Given an array cells where cells[i] == 1 if the i-th cell is occupied and cells[i] == 0
if the i-th cell is vacant, and an integer n, return the state of the prison after n days.

Example:
    Input: cells = [0,1,0,1,1,0,0,1], n = 7
    Output: [0,0,1,1,0,0,0,0]

Constraints:
- cells.length == 8
- cells[i] is either 0 or 1.
- 1 <= n <= 10^9
"""


def solution(cells, n):
    return None
