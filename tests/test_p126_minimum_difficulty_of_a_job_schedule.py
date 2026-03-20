from problems.p126_minimum_difficulty_of_a_job_schedule import solution

TEST_CASES = [
    {
        "description": "Two days, decreasing difficulty",
        "run": lambda: solution([6, 5, 4, 3, 2, 1], 2),
        "expected": 7,
    },
    {
        "description": "More days than jobs",
        "run": lambda: solution([1, 1], 3),
        "expected": -1,
    },
    {
        "description": "Three days",
        "run": lambda: solution([7, 1, 7, 1, 7, 1], 3),
        "expected": 15,
    },
    {
        "description": "Single day",
        "run": lambda: solution([3, 2, 1], 1),
        "expected": 3,
    },
    {
        "description": "Each job on its own day",
        "run": lambda: solution([1, 2, 3], 3),
        "expected": 6,
    },
]
