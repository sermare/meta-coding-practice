from problems.p186_dungeon_game import solution

TEST_CASES = [
    {
        "description": "Standard dungeon -> 7",
        "run": lambda: solution([[-2,-3,3],[-5,-10,1],[10,30,-5]]),
        "expected": 7,
    },
    {
        "description": "Single positive cell",
        "run": lambda: solution([[0]]),
        "expected": 1,
    },
    {
        "description": "Single negative cell",
        "run": lambda: solution([[-5]]),
        "expected": 6,
    },
    {
        "description": "1x3 dungeon",
        "run": lambda: solution([[-3, 5, -1]]),
        "expected": 4,
    },
]
