from problems.p294_next_greater_element_ii import solution

TEST_CASES = [
    {
        "description": "[1,2,1] -> [2,-1,2]",
        "run": lambda: solution([1, 2, 1]),
        "expected": [2, -1, 2],
    },
    {
        "description": "[1,2,3,4,3] -> [2,3,4,-1,4]",
        "run": lambda: solution([1, 2, 3, 4, 3]),
        "expected": [2, 3, 4, -1, 4],
    },
    {
        "description": "[5,4,3,2,1] -> [-1,5,5,5,5]",
        "run": lambda: solution([5, 4, 3, 2, 1]),
        "expected": [-1, 5, 5, 5, 5],
    },
    {
        "description": "[1] -> [-1]",
        "run": lambda: solution([1]),
        "expected": [-1],
    },
    {
        "description": "[3,3,3] -> [-1,-1,-1]",
        "run": lambda: solution([3, 3, 3]),
        "expected": [-1, -1, -1],
    },
]
