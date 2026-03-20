from problems.p143_meeting_rooms_ii import solution

TEST_CASES = [
    {
        "description": "Overlapping meetings need 2 rooms",
        "run": lambda: solution([[0, 30], [5, 10], [15, 20]]),
        "expected": 2,
    },
    {
        "description": "Non-overlapping meetings need 1 room",
        "run": lambda: solution([[7, 10], [2, 4]]),
        "expected": 1,
    },
    {
        "description": "All overlapping",
        "run": lambda: solution([[0, 10], [1, 5], [2, 7]]),
        "expected": 3,
    },
    {
        "description": "Single meeting",
        "run": lambda: solution([[1, 5]]),
        "expected": 1,
    },
    {
        "description": "Back to back meetings share a room",
        "run": lambda: solution([[0, 5], [5, 10], [10, 15]]),
        "expected": 1,
    },
]
