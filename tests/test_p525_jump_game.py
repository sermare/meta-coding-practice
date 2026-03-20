from problems.p525_jump_game import solution

TEST_CASES = [
    {
        "description": "Can reach end",
        "run": lambda: solution([2,3,1,1,4]),
        "expected": True,
    },
    {
        "description": "Cannot reach end",
        "run": lambda: solution([3,2,1,0,4]),
        "expected": False,
    },
    {
        "description": "Single element",
        "run": lambda: solution([0]),
        "expected": True,
    },
    {
        "description": "All ones",
        "run": lambda: solution([1,1,1,1]),
        "expected": True,
    },
    {
        "description": "First is zero",
        "run": lambda: solution([0,1]),
        "expected": False,
    },
]
