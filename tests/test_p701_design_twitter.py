from problems.p701_design_twitter import solution

TEST_CASES = [
    {
        "description": "Post and get news feed for single user",
        "run": lambda: solution(),
        "expected": None,
    },
    {
        "description": "Get feed after following another user",
        "run": lambda: solution(),
        "expected": None,
    },
    {
        "description": "Unfollow and verify feed changes",
        "run": lambda: solution(),
        "expected": None,
    },
    {
        "description": "Feed limited to 10 most recent tweets",
        "run": lambda: solution(),
        "expected": None,
    },
    {
        "description": "Empty feed for new user",
        "run": lambda: solution(),
        "expected": None,
    },
]
