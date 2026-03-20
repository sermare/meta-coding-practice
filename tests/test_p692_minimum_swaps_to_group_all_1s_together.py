from problems.p692_minimum_swaps_to_group_all_1s_together import solution

TEST_CASES = [
    {
        "description": "Basic: [1,0,1,0,1]",
        "run": lambda: solution([1, 0, 1, 0, 1]),
        "expected": 1,
    },
    {
        "description": "Already grouped: [1,1,1,0,0]",
        "run": lambda: solution([1, 1, 1, 0, 0]),
        "expected": 0,
    },
    {
        "description": "All ones: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "Spread out: [0,1,0,1,0,1,0]",
        "run": lambda: solution([0, 1, 0, 1, 0, 1, 0]),
        "expected": 1,
    },
    {
        "description": "All zeros",
        "run": lambda: solution([0, 0, 0]),
        "expected": 0,
    },
]
