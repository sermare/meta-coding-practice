from problems.p555_all_oone_data_structure import solution

TEST_CASES = [
    {
        "description": "Basic inc and getMax/getMin",
        "run": lambda: solution(
            ["inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"],
            [["hello"], ["hello"], [], [], ["leet"], [], []]
        ),
        "expected": [None, None, "hello", "hello", None, "hello", "leet"],
    },
    {
        "description": "Dec to remove key",
        "run": lambda: solution(
            ["inc", "inc", "inc", "dec", "dec", "getMaxKey"],
            [["a"], ["b"], ["b"], ["b"], ["b"], []]
        ),
        "expected": [None, None, None, None, None, "a"],
    },
    {
        "description": "Empty structure",
        "run": lambda: solution(
            ["getMaxKey", "getMinKey"],
            [[], []]
        ),
        "expected": ["", ""],
    },
    {
        "description": "Single element inc and dec",
        "run": lambda: solution(
            ["inc", "getMinKey", "dec", "getMinKey"],
            [["x"], [], ["x"], []]
        ),
        "expected": [None, "x", None, ""],
    },
]
