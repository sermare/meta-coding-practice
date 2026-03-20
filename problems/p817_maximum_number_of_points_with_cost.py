DESCRIPTION = """Maximum Number of Points with Cost

You are given an m x n integer matrix points. Starting with 0 points, you want
to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at
coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you
picked in the previous row. For every two adjacent rows r and r + 1, picking
cells at (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

Example:
    Input: points = [[1,2,3],[1,5,1],[3,1,1]]
    Output: 9

"""


def solution(points):
    return None
