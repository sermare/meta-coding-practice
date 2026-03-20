from problems.p808_find_valid_matrix_given_row_and_column_sums import solution

def _validate(matrix, rowSum, colSum):
    if matrix is None:
        return False
    for i, row in enumerate(matrix):
        if sum(row) != rowSum[i]:
            return False
    for j in range(len(colSum)):
        if sum(matrix[i][j] for i in range(len(rowSum))) != colSum[j]:
            return False
    return True

TEST_CASES = [
    {
        "description": "2x2 matrix: rowSum=[3,8] colSum=[4,7]",
        "run": lambda: _validate(solution([3,8], [4,7]), [3,8], [4,7]),
        "expected": True,
    },
    {
        "description": "3x2 matrix: rowSum=[5,7,10] colSum=[8,14]",
        "run": lambda: _validate(solution([5,7,10], [8,14]), [5,7,10], [8,14]),
        "expected": True,
    },
    {
        "description": "1x1 matrix: rowSum=[5] colSum=[5]",
        "run": lambda: _validate(solution([5], [5]), [5], [5]),
        "expected": True,
    },
    {
        "description": "Zero sums: rowSum=[0,0] colSum=[0,0]",
        "run": lambda: solution([0,0], [0,0]),
        "expected": [[0,0],[0,0]],
    },
]
