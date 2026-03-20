from problems.p704_count_good_meals import solution

TEST_CASES = [
    {
        "description": "Basic case: [1,3,5,7,9]",
        "run": lambda: solution([1, 3, 5, 7, 9]),
        "expected": 4,
    },
    {
        "description": "Duplicate values: [1,1,1,3,3,3,7]",
        "run": lambda: solution([1, 1, 1, 3, 3, 3, 7]),
        "expected": 15,
    },
    {
        "description": "Single pair: [0,1]",
        "run": lambda: solution([0, 1]),
        "expected": 0,
    },
    {
        "description": "Powers of two sums: [2,2]",
        "run": lambda: solution([2, 2]),
        "expected": 1,
    },
    {
        "description": "Empty array",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
