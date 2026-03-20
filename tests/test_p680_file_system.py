from problems.p680_file_system import solution

TEST_CASES = [
    {
        "description": "Create and get",
        "run": lambda: solution(["create /a 1", "get /a"]),
        "expected": [True, 1],
    },
    {
        "description": "Create nested path",
        "run": lambda: solution(["create /a 1", "create /a/b 2", "get /a/b"]),
        "expected": [True, True, 2],
    },
    {
        "description": "Parent does not exist",
        "run": lambda: solution(["create /a/b 1"]),
        "expected": [False],
    },
    {
        "description": "Get nonexistent path",
        "run": lambda: solution(["get /z"]),
        "expected": [-1],
    },
]
