from problems.p379_course_schedule_ii import solution


TEST_CASES = [
    {
        "description": "Simple order",
        "run": lambda: solution(2, [[1, 0]]),
        "expected": [0, 1],
    },
    {
        "description": "No prerequisites",
        "run": lambda: solution(1, []),
        "expected": [0],
    },
    {
        "description": "Cycle: impossible",
        "run": lambda: solution(2, [[1, 0], [0, 1]]),
        "expected": [],
    },
    {
        "description": "Multiple valid orders (check length)",
        "run": lambda: len(solution(4, [[1, 0], [2, 0], [3, 1], [3, 2]])),
        "expected": 4,
    },
]
