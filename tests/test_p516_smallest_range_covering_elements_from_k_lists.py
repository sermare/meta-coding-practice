from problems.p516_smallest_range_covering_elements_from_k_lists import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]),
        "expected": [20, 24],
    },
    {
        "description": "Single element lists",
        "run": lambda: solution([[1],[2],[3]]),
        "expected": [1, 3],
    },
    {
        "description": "Overlapping",
        "run": lambda: solution([[1,2,3],[1,2,3],[1,2,3]]),
        "expected": [1, 1],
    },
    {
        "description": "Two lists",
        "run": lambda: solution([[1,5,9],[4,8,12]]),
        "expected": [4, 5],
    },
]
