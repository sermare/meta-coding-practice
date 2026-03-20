from problems.p050_simplify_path import solution

TEST_CASES = [
    {
        "description": "/home/ -> /home",
        "run": lambda: solution("/home/"),
        "expected": "/home",
    },
    {
        "description": "/../ -> /",
        "run": lambda: solution("/../"),
        "expected": "/",
    },
    {
        "description": "/home//foo/ -> /home/foo",
        "run": lambda: solution("/home//foo/"),
        "expected": "/home/foo",
    },
    {
        "description": "/a/./b/../../c/ -> /c",
        "run": lambda: solution("/a/./b/../../c/"),
        "expected": "/c",
    },
    {
        "description": "/a/b/c/../d -> /a/b/d",
        "run": lambda: solution("/a/b/c/../d"),
        "expected": "/a/b/d",
    },
]
