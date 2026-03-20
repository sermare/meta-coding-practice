from problems.p789_count_collisions_on_a_road import solution

TEST_CASES = [
    {
        "description": "Basic: RLRSLL",
        "run": lambda: solution("RLRSLL"),
        "expected": 5,
    },
    {
        "description": "No collisions: LLLL",
        "run": lambda: solution("LLLL"),
        "expected": 0,
    },
    {
        "description": "No collisions: RRRR",
        "run": lambda: solution("RRRR"),
        "expected": 0,
    },
    {
        "description": "All stationary: SSSS",
        "run": lambda: solution("SSSS"),
        "expected": 0,
    },
    {
        "description": "Simple collision: RL",
        "run": lambda: solution("RL"),
        "expected": 2,
    },
]
