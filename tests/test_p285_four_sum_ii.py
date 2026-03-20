from problems.p285_four_sum_ii import solution

TEST_CASES = [
    {
        "description": "[1,2],[-2,-1],[-1,2],[0,2] -> 2",
        "run": lambda: solution([1, 2], [-2, -1], [-1, 2], [0, 2]),
        "expected": 2,
    },
    {
        "description": "[0],[0],[0],[0] -> 1",
        "run": lambda: solution([0], [0], [0], [0]),
        "expected": 1,
    },
    {
        "description": "[1],[-1],[0],[0] -> 1",
        "run": lambda: solution([1], [-1], [0], [0]),
        "expected": 1,
    },
    {
        "description": "[1],[1],[1],[1] -> 0",
        "run": lambda: solution([1], [1], [1], [1]),
        "expected": 0,
    },
]
