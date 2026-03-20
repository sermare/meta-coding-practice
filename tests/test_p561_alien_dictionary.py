from problems.p561_alien_dictionary import solution

TEST_CASES = [
    {
        "description": "Standard case: wertf",
        "run": lambda: solution(["wrt", "wrf", "er", "ett", "rftt"]),
        "expected": "wertf",
    },
    {
        "description": "Two words: zx",
        "run": lambda: solution(["z", "x"]),
        "expected": "zx",
    },
    {
        "description": "Invalid ordering: z,x,z",
        "run": lambda: solution(["z", "x", "z"]),
        "expected": "",
    },
    {
        "description": "Single word",
        "run": lambda: solution(["abc"]),
        "expected": "abc",
    },
]
