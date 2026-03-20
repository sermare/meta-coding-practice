from problems.p345_max_consecutive_ones_iii import solution

TEST_CASES = [
    {
        "description": "Basic: [1,1,1,0,0,0,1,1,1,1,0] k=2 -> 6",
        "run": lambda: solution([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
        "expected": 6,
    },
    {
        "description": "Longer: k=3 -> 10",
        "run": lambda: solution([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
        "expected": 10,
    },
    {
        "description": "All ones: [1,1,1] k=0 -> 3",
        "run": lambda: solution([1, 1, 1], 0),
        "expected": 3,
    },
    {
        "description": "All zeros: [0,0,0] k=2 -> 2",
        "run": lambda: solution([0, 0, 0], 2),
        "expected": 2,
    },
]
