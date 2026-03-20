from problems.p088_time_based_key-value_store import solution

TEST_CASES = [
    {
        "description": "Basic set and get operations",
        "run": lambda: solution(
            ["TimeMap", "set", "get", "get", "set", "get"],
            [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4]]
        ),
        "expected": [None, None, "bar", "bar", None, "bar2"],
    },
    {
        "description": "Get before any set for key",
        "run": lambda: solution(
            ["TimeMap", "get"],
            [[], ["foo", 1]]
        ),
        "expected": [None, ""],
    },
    {
        "description": "Get with exact timestamp",
        "run": lambda: solution(
            ["TimeMap", "set", "get"],
            [[], ["key", "val", 5], ["key", 5]]
        ),
        "expected": [None, None, "val"],
    },
    {
        "description": "Multiple keys",
        "run": lambda: solution(
            ["TimeMap", "set", "set", "get", "get"],
            [[], ["a", "v1", 1], ["b", "v2", 2], ["a", 1], ["b", 2]]
        ),
        "expected": [None, None, None, "v1", "v2"],
    },
]
