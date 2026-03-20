from problems.p095_word_ladder import solution

TEST_CASES = [
    {
        "description": "Standard: hit -> cog",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        "expected": 5,
    },
    {
        "description": "No path: endWord not in list",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
        "expected": 0,
    },
    {
        "description": "Direct neighbor",
        "run": lambda: solution("hot", "dot", ["dot"]),
        "expected": 2,
    },
    {
        "description": "No transformation possible",
        "run": lambda: solution("abc", "xyz", ["xyz"]),
        "expected": 0,
    },
]
