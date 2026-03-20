from problems.p603_can_place_flowers import solution

TEST_CASES = [
    {
        "description": "Can place 1 flower: [1,0,0,0,1]",
        "run": lambda: solution([1, 0, 0, 0, 1], 1),
        "expected": True,
    },
    {
        "description": "Cannot place 2 flowers: [1,0,0,0,1]",
        "run": lambda: solution([1, 0, 0, 0, 1], 2),
        "expected": False,
    },
    {
        "description": "Empty bed place 1: [0,0,0]",
        "run": lambda: solution([0, 0, 0], 1),
        "expected": True,
    },
    {
        "description": "No flowers needed: [1,0,1]",
        "run": lambda: solution([1, 0, 1], 0),
        "expected": True,
    },
    {
        "description": "Single empty plot: [0]",
        "run": lambda: solution([0], 1),
        "expected": True,
    },
]
