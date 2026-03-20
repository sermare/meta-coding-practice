from problems.p668_minimum_knight_moves import solution

TEST_CASES = [
    {
        "description": "One move: (2,1)",
        "run": lambda: solution(2, 1),
        "expected": 1,
    },
    {
        "description": "Origin: (0,0)",
        "run": lambda: solution(0, 0),
        "expected": 0,
    },
    {
        "description": "Symmetric: (5,5)",
        "run": lambda: solution(5, 5),
        "expected": 4,
    },
    {
        "description": "Far target: (1,1)",
        "run": lambda: solution(1, 1),
        "expected": 2,
    },
]
