DESCRIPTION = """Game of Life

According to Wikipedia's article on Conway's Game of Life, the board is made up of an
m x n grid of cells, where each cell has an initial state: live (1) or dead (0). Each
cell interacts with its eight neighbors using the following rules:
1. Any live cell with fewer than two live neighbors dies (under-population).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (over-population).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

Given the current state of the board, return the next state.

Example:
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]
"""


def solution(board):
    return None
