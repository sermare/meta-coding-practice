DESCRIPTION = """
Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in
a diagonal order.

The traversal starts from the top-left element. For even-numbered diagonals
(0, 2, 4, ...), traverse upward (bottom-left to top-right). For odd-numbered
diagonals (1, 3, 5, ...), traverse downward (top-right to bottom-left).

Constraints:
  - m == mat.length
  - n == mat[i].length
  - 1 <= m, n <= 10^4
  - 1 <= m * n <= 10^4
  - -10^5 <= mat[i][j] <= 10^5

Examples:
  Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
  Output: [1,2,4,7,5,3,6,8,9]

  Input: mat = [[1,2],[3,4]]
  Output: [1,2,3,4]
""".strip()


def solution(mat):
    return None
