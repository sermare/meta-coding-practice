from problems.p069_set_matrix_zeroes import solution

TEST_CASES = [
    {
        "description": "3x3 with one zero",
        "run": lambda: (lambda m: (solution(m), m))([[1, 1, 1], [1, 0, 1], [1, 1, 1]])[1],
        "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    },
    {
        "description": "3x4 with corner zeroes",
        "run": lambda: (lambda m: (solution(m), m))([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])[1],
        "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    },
    {
        "description": "No zeroes",
        "run": lambda: (lambda m: (solution(m), m))([[1, 2], [3, 4]])[1],
        "expected": [[1, 2], [3, 4]],
    },
    {
        "description": "All zeroes",
        "run": lambda: (lambda m: (solution(m), m))([[0, 0], [0, 0]])[1],
        "expected": [[0, 0], [0, 0]],
    },
]
