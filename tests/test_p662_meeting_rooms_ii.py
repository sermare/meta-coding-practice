from problems.p662_meeting_rooms_ii import solution

TEST_CASES = [
    {
        "description": "Need two rooms",
        "run": lambda: solution([[0, 30], [5, 10], [15, 20]]),
        "expected": 2,
    },
    {
        "description": "Sequential meetings need one room",
        "run": lambda: solution([[7, 10], [2, 4]]),
        "expected": 1,
    },
    {
        "description": "All overlapping need three rooms",
        "run": lambda: solution([[1, 10], [2, 7], [3, 5]]),
        "expected": 3,
    },
    {
        "description": "Empty input",
        "run": lambda: solution([]),
        "expected": 0,
    },
    {
        "description": "Adjacent meetings share room",
        "run": lambda: solution([[1, 5], [5, 10], [10, 15]]),
        "expected": 1,
    },
]
