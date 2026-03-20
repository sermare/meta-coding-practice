DESCRIPTION = """Image Smoother

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an
image by rounding down the average of the cell and the eight surrounding cells. If one
or more of the surrounding cells of a cell is not present, we do not consider it in the
average.

Given an m x n integer matrix img representing the grayscale of an image, return the
image after applying the smoother on each cell of it.

Example:
    Input: img = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[0,0,0],[0,0,0],[0,0,0]]
    Explanation: For every cell, the average of all 9 cells is 0.888... rounded down to 0.
"""


def solution(img):
    return None
