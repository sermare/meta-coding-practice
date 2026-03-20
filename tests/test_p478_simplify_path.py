from problems.p478_simplify_path import solution

TEST_CASES = [
    {
        "description": "Trailing slash: "/home/" -> "/home"",
        "run": lambda: solution("/home/"),
        "expected": "/home",
    },
    {
        "description": "Double slash: "/home//foo/"",
        "run": lambda: solution("/home//foo/"),
        "expected": "/home/foo",
    },
    {
        "description": "Parent dir: "../Pictures"",
        "run": lambda: solution("/home/user/Documents/../Pictures"),
        "expected": "/home/user/Pictures",
    },
    {
        "description": "Root parent: "/../"",
        "run": lambda: solution("/../"),
        "expected": "/",
    },
    {
        "description": "Current dir: "/a/./b"",
        "run": lambda: solution("/a/./b"),
        "expected": "/a/b",
    },
]
