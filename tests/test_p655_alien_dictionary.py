from problems.p655_alien_dictionary import solution

TEST_CASES = [
    {
        "description": "Standard case: wrt, wrf, er, ett, rftt",
        "run": lambda: solution(["wrt", "wrf", "er", "ett", "rftt"]),
        "expected": "wertf",
    },
    {
        "description": "Simple two-word case",
        "run": lambda: solution(["z", "x"]),
        "expected": "zx",
    },
    {
        "description": "Invalid order returns empty",
        "run": lambda: solution(["z", "x", "z"]),
        "expected": "",
    },
    {
        "description": "Single word",
        "run": lambda: solution(["abc"]),
        "expected": "abc",
    },
]
