from problems.p173_spiral_matrix_iii import solution

TEST_CASES = [
    {
        "description": "1x4 grid starting at (0,0)",
        "run": lambda: solution(1, 4, 0, 0),
        "expected": [[0,0],[0,1],[0,2],[0,3]],
    },
    {
        "description": "1x1 grid",
        "run": lambda: solution(1, 1, 0, 0),
        "expected": [[0, 0]],
    },
    {
        "description": "2x2 grid starting at (0,0)",
        "run": lambda: solution(2, 2, 0, 0),
        "expected": [[0,0],[0,1],[1,1],[1,0]],
    },
    {
        "description": "Result length equals rows*cols",
        "run": lambda: len(solution(3, 3, 1, 1)),
        "expected": 9,
    },
]
