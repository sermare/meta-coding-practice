from problems.p136_keys_and_rooms import solution

TEST_CASES = [
    {
        "description": "All rooms reachable in chain",
        "run": lambda: solution([[1], [2], [3], []]),
        "expected": True,
    },
    {
        "description": "Room 2 unreachable",
        "run": lambda: solution([[1, 3], [3, 0, 1], [2], [0]]),
        "expected": False,
    },
    {
        "description": "All keys in first room",
        "run": lambda: solution([[1, 2, 3], [], [], []]),
        "expected": True,
    },
    {
        "description": "Two rooms, key available",
        "run": lambda: solution([[1], []]),
        "expected": True,
    },
    {
        "description": "Circular keys",
        "run": lambda: solution([[1], [2], [0]]),
        "expected": True,
    },
]
