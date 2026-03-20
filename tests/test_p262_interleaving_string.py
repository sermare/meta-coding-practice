from problems.p262_interleaving_string import solution

TEST_CASES = [
    {
        "description": "'aabcc','dbbca','aadbbcbcac' -> True",
        "run": lambda: solution("aabcc", "dbbca", "aadbbcbcac"),
        "expected": True,
    },
    {
        "description": "'aabcc','dbbca','aadbbbaccc' -> False",
        "run": lambda: solution("aabcc", "dbbca", "aadbbbaccc"),
        "expected": False,
    },
    {
        "description": "Empty strings -> True",
        "run": lambda: solution("", "", ""),
        "expected": True,
    },
    {
        "description": "'a','','a' -> True",
        "run": lambda: solution("a", "", "a"),
        "expected": True,
    },
    {
        "description": "'ab','cd','acbd' -> True",
        "run": lambda: solution("ab", "cd", "acbd"),
        "expected": True,
    },
]
