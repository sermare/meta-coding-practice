from problems.p212_design_hashmap import solution

TEST_CASES = [
    {
        "description": "Basic put, get, remove",
        "run": lambda: solution(["put", "put", "get", "get", "put", "get", "remove", "get"],
                                [[1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]),
        "expected": [None, None, 1, -1, None, 1, None, -1],
    },
    {
        "description": "Overwrite existing key",
        "run": lambda: solution(["put", "put", "get"], [[1, 10], [1, 20], [1]]),
        "expected": [None, None, 20],
    },
    {
        "description": "Remove non-existent key",
        "run": lambda: solution(["remove", "get"], [[5], [5]]),
        "expected": [None, -1],
    },
    {
        "description": "Multiple keys",
        "run": lambda: solution(["put", "put", "put", "get", "get", "get"],
                                [[1, 1], [2, 2], [3, 3], [1], [2], [3]]),
        "expected": [None, None, None, 1, 2, 3],
    },
]
