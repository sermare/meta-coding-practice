from problems.p388_alien_dictionary import solution


TEST_CASES = [
    {
        "description": "Standard alien ordering",
        "run": lambda: solution(["wrt", "wrf", "er", "ett", "rftt"]),
        "expected": "wertf",
    },
    {
        "description": "Two words",
        "run": lambda: solution(["z", "x"]),
        "expected": "zx",
    },
    {
        "description": "Invalid order",
        "run": lambda: solution(["z", "x", "z"]),
        "expected": "",
    },
    {
        "description": "Single word",
        "run": lambda: len(solution(["abc"])),
        "expected": 3,
    },
]
