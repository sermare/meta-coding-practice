from problems.p195_majority_element_ii import solution

TEST_CASES = [
    {
        "description": "[3,2,3] -> [3]",
        "run": lambda: sorted(solution([3, 2, 3])),
        "expected": [3],
    },
    {
        "description": "[1] -> [1]",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "[1,2] -> [1,2]",
        "run": lambda: sorted(solution([1, 2])),
        "expected": [1, 2],
    },
    {
        "description": "[2,2,1,3] -> [2]",
        "run": lambda: solution([2, 2, 1, 3]),
        "expected": [2],
    },
]
