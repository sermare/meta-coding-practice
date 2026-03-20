from problems.p064_jump_game import solution

TEST_CASES = [
    {
        "description": "Can reach end: [2,3,1,1,4]",
        "run": lambda: solution([2, 3, 1, 1, 4]),
        "expected": True,
    },
    {
        "description": "Cannot reach end: [3,2,1,0,4]",
        "run": lambda: solution([3, 2, 1, 0, 4]),
        "expected": False,
    },
    {
        "description": "Single element: [0]",
        "run": lambda: solution([0]),
        "expected": True,
    },
    {
        "description": "All ones: [1,1,1,1]",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": True,
    },
    {
        "description": "Large first jump: [5,0,0,0,0]",
        "run": lambda: solution([5, 0, 0, 0, 0]),
        "expected": True,
    },
]
