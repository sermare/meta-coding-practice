from problems.p526_jump_game_ii import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([2,3,1,1,4]),
        "expected": 2,
    },
    {
        "description": "Optimal jumps",
        "run": lambda: solution([2,3,0,1,4]),
        "expected": 2,
    },
    {
        "description": "Single element",
        "run": lambda: solution([0]),
        "expected": 0,
    },
    {
        "description": "Direct jump",
        "run": lambda: solution([5,1,1,1,1]),
        "expected": 1,
    },
    {
        "description": "Step by step",
        "run": lambda: solution([1,1,1,1]),
        "expected": 3,
    },
]
