from problems.p114_design_add_and_search_words import solution

TEST_CASES = [
    {
        "description": "Standard add and search with dots",
        "run": lambda: solution(
            ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
            [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        ),
        "expected": [None, None, None, None, False, True, True, True],
    },
    {
        "description": "Empty search",
        "run": lambda: solution(
            ["WordDictionary","search"],
            [[],["a"]]
        ),
        "expected": [None, False],
    },
    {
        "description": "All dots search",
        "run": lambda: solution(
            ["WordDictionary","addWord","search","search"],
            [[],["abc"],["..."],["....."]]
        ),
        "expected": [None, None, True, False],
    },
    {
        "description": "Exact match only",
        "run": lambda: solution(
            ["WordDictionary","addWord","search","search"],
            [[],["hello"],["hello"],["hell"]]
        ),
        "expected": [None, None, True, False],
    },
]
