from problems.p378_course_schedule import solution


TEST_CASES = [
    {
        "description": "Simple prerequisite: possible",
        "run": lambda: solution(2, [[1, 0]]),
        "expected": True,
    },
    {
        "description": "Cycle: impossible",
        "run": lambda: solution(2, [[1, 0], [0, 1]]),
        "expected": False,
    },
    {
        "description": "No prerequisites",
        "run": lambda: solution(3, []),
        "expected": True,
    },
    {
        "description": "Chain of prerequisites",
        "run": lambda: solution(4, [[1, 0], [2, 1], [3, 2]]),
        "expected": True,
    },
    {
        "description": "Longer cycle",
        "run": lambda: solution(3, [[0, 1], [1, 2], [2, 0]]),
        "expected": False,
    },
]
