from problems.p383_word_ladder import solution


TEST_CASES = [
    {
        "description": "Standard transformation: length 5",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        "expected": 5,
    },
    {
        "description": "No valid transformation",
        "run": lambda: solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
        "expected": 0,
    },
    {
        "description": "Direct one-step transform",
        "run": lambda: solution("hot", "dot", ["dot"]),
        "expected": 2,
    },
    {
        "description": "No path possible",
        "run": lambda: solution("abc", "xyz", ["abd", "abe"]),
        "expected": 0,
    },
]
