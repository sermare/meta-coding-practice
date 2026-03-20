from problems.p611_all_oone_data_structure import solution

TEST_CASES = [
    {
        "description": "Basic inc and get operations",
        "run": lambda: solution(
            ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey"],
            [[], ["hello"], ["hello"], [], [], ["leet"], []]
        ),
        "expected": [None, None, None, "hello", "hello", None, "hello"],
    },
    {
        "description": "Inc and dec operations",
        "run": lambda: solution(
            ["AllOne", "inc", "inc", "inc", "dec", "getMaxKey", "getMinKey"],
            [[], ["a"], ["b"], ["a"], ["a"], [], []]
        ),
        "expected": [None, None, None, None, None, "a", "b"],
    },
    {
        "description": "Empty structure getMaxKey",
        "run": lambda: solution(
            ["AllOne", "getMaxKey"],
            [[], []]
        ),
        "expected": [None, ""],
    },
    {
        "description": "Empty structure getMinKey",
        "run": lambda: solution(
            ["AllOne", "getMinKey"],
            [[], []]
        ),
        "expected": [None, ""],
    },
]
