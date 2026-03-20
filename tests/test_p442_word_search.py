from problems.p442_word_search import solution

TEST_CASES = [
    {
        "description": "Found: ABCCED",
        "run": lambda: solution([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        "expected": True,
    },
    {
        "description": "Found: SEE",
        "run": lambda: solution([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        "expected": True,
    },
    {
        "description": "Not found: ABCB",
        "run": lambda: solution([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),
        "expected": False,
    },
    {
        "description": "Single cell match: A",
        "run": lambda: solution([["A"]], "A"),
        "expected": True,
    },
    {
        "description": "Single cell no match: A vs B",
        "run": lambda: solution([["A"]], "B"),
        "expected": False,
    },
]
