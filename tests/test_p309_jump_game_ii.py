from problems.p309_jump_game_ii import solution

TEST_CASES = [
    {
        "description": "Basic: [2,3,1,1,4] -> 2",
        "run": lambda: solution([2, 3, 1, 1, 4]),
        "expected": 2,
    },
    {
        "description": "Greedy: [2,3,0,1,4] -> 2",
        "run": lambda: solution([2, 3, 0, 1, 4]),
        "expected": 2,
    },
    {
        "description": "Single element: [0] -> 0",
        "run": lambda: solution([0]),
        "expected": 0,
    },
    {
        "description": "All ones: [1,1,1,1] -> 3",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 3,
    },
]
