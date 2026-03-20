from problems.p550_robot_bounded_in_circle import solution

TEST_CASES = [
    {
        "description": "Returns to origin",
        "run": lambda: solution("GGLLGG"),
        "expected": True,
    },
    {
        "description": "Goes forever",
        "run": lambda: solution("GG"),
        "expected": False,
    },
    {
        "description": "Left turn cycle",
        "run": lambda: solution("GL"),
        "expected": True,
    },
    {
        "description": "Right turn cycle",
        "run": lambda: solution("GR"),
        "expected": True,
    },
    {
        "description": "No movement",
        "run": lambda: solution("LLLL"),
        "expected": True,
    },
]
