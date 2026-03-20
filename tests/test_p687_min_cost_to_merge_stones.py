from problems.p687_min_cost_to_merge_stones import solution

TEST_CASES = [
    {
        "description": "Basic k=2: [3,2,4,1]",
        "run": lambda: solution([3, 2, 4, 1], 2),
        "expected": 20,
    },
    {
        "description": "Impossible case: [3,2,4,1] k=3",
        "run": lambda: solution([3, 2, 4, 1], 3),
        "expected": -1,
    },
    {
        "description": "k=3 possible: [3,5,1,2,6]",
        "run": lambda: solution([3, 5, 1, 2, 6], 3),
        "expected": 25,
    },
    {
        "description": "Single pile",
        "run": lambda: solution([5], 2),
        "expected": 0,
    },
]
