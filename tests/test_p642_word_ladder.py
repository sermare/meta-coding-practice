from problems.p642_word_ladder import solution

TEST_CASES = [
    {
        "description": "Standard path: hit -> cog",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        "expected": 5,
    },
    {
        "description": "No path: hit -> cog without cog",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
        "expected": 0,
    },
    {
        "description": "Direct transformation",
        "run": lambda: solution("hot", "dot", ["dot"]),
        "expected": 2,
    },
    {
        "description": "No transformation possible",
        "run": lambda: solution("abc", "xyz", ["def"]),
        "expected": 0,
    },
]
