from problems.p124_robot_bounded_in_circle import solution

TEST_CASES = [
    {
        "description": "Returns to origin",
        "run": lambda: solution("GGLLGG"),
        "expected": True,
    },
    {
        "description": "Goes straight forever",
        "run": lambda: solution("GG"),
        "expected": False,
    },
    {
        "description": "Turns left, faces different direction",
        "run": lambda: solution("GL"),
        "expected": True,
    },
    {
        "description": "Full circle with right turns",
        "run": lambda: solution("GRGRGRG"),
        "expected": True,
    },
    {
        "description": "Complex bounded path",
        "run": lambda: solution("GLGLGGLGL"),
        "expected": True,
    },
]
