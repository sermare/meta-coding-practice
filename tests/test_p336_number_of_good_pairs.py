from problems.p336_number_of_good_pairs import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,1,1,3] -> 4",
        "run": lambda: solution([1, 2, 3, 1, 1, 3]),
        "expected": 4,
    },
    {
        "description": "All same: [1,1,1,1] -> 6",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 6,
    },
    {
        "description": "All different: [1,2,3] -> 0",
        "run": lambda: solution([1, 2, 3]),
        "expected": 0,
    },
    {
        "description": "Two elements same: [1,1] -> 1",
        "run": lambda: solution([1, 1]),
        "expected": 1,
    },
]
