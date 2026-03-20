from problems.p732_stone_game_vii import solution

TEST_CASES = [
    {
        "description": "Basic case: [5,3,1,4,2]",
        "run": lambda: solution([5, 3, 1, 4, 2]),
        "expected": 6,
    },
    {
        "description": "Two stones: [7,90]",
        "run": lambda: solution([7, 90]),
        "expected": 83,
    },
    {
        "description": "Equal stones: [1,1,1]",
        "run": lambda: solution([1, 1, 1]),
        "expected": 1,
    },
    {
        "description": "Increasing: [1,2,3,4]",
        "run": lambda: solution([1, 2, 3, 4]),
        "expected": 4,
    },
]
