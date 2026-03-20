DESCRIPTION = """Candy Crush

Given an m x n integer matrix `board` representing a candy crush board, perform the
candy crush operation repeatedly until the board is stable:
1. Find all groups of 3 or more consecutive same candies (horizontal or vertical).
2. Remove all found candies at the same time (set to 0).
3. Drop remaining candies down to fill empty spaces.
Repeat until no more candies can be crushed.

Return the final stable board.

Example:
    Input: board = [
        [110,5,112,113,114],
        [210,211,5,213,214],
        [310,311,3,313,314],
        [410,411,412,5,414],
        [5,1,512,3,3],
        [610,4,1,613,614],
        [710,1,2,713,714],
        [810,1,2,1,1],
        [1,1,2,2,2],
        [4,1,4,4,1014]
    ]
    Output: (stable board after all crushing)
"""


def solution(board):
    return None
