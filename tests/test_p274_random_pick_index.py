from problems.p274_random_pick_index import solution

TEST_CASES = [
    {
        "description": "[1,2,3,3,3] target=3 -> index in {2,3,4}",
        "run": lambda: solution([1, 2, 3, 3, 3], 3) in {2, 3, 4},
        "expected": True,
    },
    {
        "description": "[1] target=1 -> 0",
        "run": lambda: solution([1], 1),
        "expected": 0,
    },
    {
        "description": "[1,2,3] target=1 -> 0",
        "run": lambda: solution([1, 2, 3], 1),
        "expected": 0,
    },
    {
        "description": "[5,5,5,5] target=5 -> index in {0,1,2,3}",
        "run": lambda: solution([5, 5, 5, 5], 5) in {0, 1, 2, 3},
        "expected": True,
    },
]
