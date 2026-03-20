from problems.p430_interleaving_string import solution

TEST_CASES = [
    {
        "description": "Basic interleave: aabcc, dbbca, aadbbcbcac",
        "run": lambda: solution("aabcc", "dbbca", "aadbbcbcac"),
        "expected": True,
    },
    {
        "description": "Not interleaved: aabcc, dbbca, aadbbbaccc",
        "run": lambda: solution("aabcc", "dbbca", "aadbbbaccc"),
        "expected": False,
    },
    {
        "description": "Empty strings",
        "run": lambda: solution("", "", ""),
        "expected": True,
    },
    {
        "description": "One empty: '', a, a",
        "run": lambda: solution("", "a", "a"),
        "expected": True,
    },
    {
        "description": "Simple: ab, cd, acbd",
        "run": lambda: solution("ab", "cd", "acbd"),
        "expected": True,
    },
]
