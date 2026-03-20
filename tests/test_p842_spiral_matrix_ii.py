from problems.p842_spiral_matrix_ii import solution

TEST_CASES = [
    {
        "description": "3x3 spiral",
        "run": lambda: solution(3),
        "expected": [[1,2,3],[8,9,4],[7,6,5]],
    },
    {
        "description": "1x1 spiral",
        "run": lambda: solution(1),
        "expected": [[1]],
    },
    {
        "description": "2x2 spiral",
        "run": lambda: solution(2),
        "expected": [[1,2],[4,3]],
    },
    {
        "description": "4x4 spiral",
        "run": lambda: solution(4),
        "expected": [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]],
    },
]
