from problems.p679_find_median_from_data_stream import solution

TEST_CASES = [
    {
        "description": "Basic add and find",
        "run": lambda: solution(["add 1", "add 2", "find", "add 3", "find"]),
        "expected": [1.5, 2.0],
    },
    {
        "description": "Single element median",
        "run": lambda: solution(["add 5", "find"]),
        "expected": [5.0],
    },
    {
        "description": "Odd number of elements",
        "run": lambda: solution(["add 1", "add 2", "add 3", "find"]),
        "expected": [2.0],
    },
    {
        "description": "Decreasing order",
        "run": lambda: solution(["add 3", "add 2", "add 1", "find"]),
        "expected": [2.0],
    },
]
