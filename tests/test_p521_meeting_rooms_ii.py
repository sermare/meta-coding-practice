from problems.p521_meeting_rooms_ii import solution

TEST_CASES = [
    {
        "description": "Two rooms needed",
        "run": lambda: solution([[0,30],[5,10],[15,20]]),
        "expected": 2,
    },
    {
        "description": "One room enough",
        "run": lambda: solution([[7,10],[2,4]]),
        "expected": 1,
    },
    {
        "description": "Three rooms",
        "run": lambda: solution([[0,10],[5,15],[10,20],[5,10]]),
        "expected": 3,
    },
    {
        "description": "Empty schedule",
        "run": lambda: solution([]),
        "expected": 0,
    },
    {
        "description": "No overlap",
        "run": lambda: solution([[1,2],[3,4],[5,6]]),
        "expected": 1,
    },
]
