from problems.p528_hand_of_straights import solution

TEST_CASES = [
    {
        "description": "Basic valid",
        "run": lambda: solution([1,2,3,6,2,3,4,7,8], 3),
        "expected": True,
    },
    {
        "description": "Invalid grouping",
        "run": lambda: solution([1,2,3,4,5], 4),
        "expected": False,
    },
    {
        "description": "Group size 1",
        "run": lambda: solution([1,2,3], 1),
        "expected": True,
    },
    {
        "description": "Single group",
        "run": lambda: solution([1,2,3], 3),
        "expected": True,
    },
    {
        "description": "Impossible gap",
        "run": lambda: solution([1,2,4,5], 2),
        "expected": False,
    },
]
