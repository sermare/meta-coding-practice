from problems.p040_next_permutation import solution

TEST_CASES = [
    {
        "description": "[1,2,3] -> [1,3,2]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 3, 2],
    },
    {
        "description": "[3,2,1] -> [1,2,3] (last permutation wraps around)",
        "run": lambda: solution([3, 2, 1]),
        "expected": [1, 2, 3],
    },
    {
        "description": "[1,1,5] -> [1,5,1]",
        "run": lambda: solution([1, 1, 5]),
        "expected": [1, 5, 1],
    },
    {
        "description": "[1] -> [1] (single element)",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "[1,3,2] -> [2,1,3]",
        "run": lambda: solution([1, 3, 2]),
        "expected": [2, 1, 3],
    },
]
