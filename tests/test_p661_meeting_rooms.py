from problems.p661_meeting_rooms import solution

TEST_CASES = [
    {
        "description": "Overlapping meetings",
        "run": lambda: solution([[0, 30], [5, 10], [15, 20]]),
        "expected": False,
    },
    {
        "description": "No overlapping meetings",
        "run": lambda: solution([[7, 10], [2, 4]]),
        "expected": True,
    },
    {
        "description": "Empty schedule",
        "run": lambda: solution([]),
        "expected": True,
    },
    {
        "description": "Single meeting",
        "run": lambda: solution([[1, 5]]),
        "expected": True,
    },
    {
        "description": "Adjacent meetings (no overlap)",
        "run": lambda: solution([[1, 5], [5, 10]]),
        "expected": True,
    },
]
