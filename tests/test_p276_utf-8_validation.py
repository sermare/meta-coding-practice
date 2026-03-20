from problems.p276_utf-8_validation import solution

TEST_CASES = [
    {
        "description": "[197,130,1] -> True",
        "run": lambda: solution([197, 130, 1]),
        "expected": True,
    },
    {
        "description": "[235,140,4] -> False",
        "run": lambda: solution([235, 140, 4]),
        "expected": False,
    },
    {
        "description": "[0] -> True (1-byte ASCII)",
        "run": lambda: solution([0]),
        "expected": True,
    },
    {
        "description": "[248,130,130,130] -> False (5-byte not valid)",
        "run": lambda: solution([248, 130, 130, 130]),
        "expected": False,
    },
    {
        "description": "[230,136,145] -> True (3-byte char)",
        "run": lambda: solution([230, 136, 145]),
        "expected": True,
    },
]
