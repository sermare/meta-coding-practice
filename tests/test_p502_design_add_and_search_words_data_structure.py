from problems.p502_design_add_and_search_words_data_structure import solution

TEST_CASES = [
    {
        "description": "Basic add and search",
        "run": lambda: solution(["WordDictionary","addWord","addWord","addWord","search","search","search","search"], [[],["bad"],["dad"],["mad"],[".ad"],["b.."],["b.d"],["..."]]),
        "expected": [None, None, None, None, True, True, True, True],
    },
    {
        "description": "No match",
        "run": lambda: solution(["WordDictionary","addWord","search"], [[],["hello"],["world"]]),
        "expected": [None, None, False],
    },
    {
        "description": "Dot pattern no match",
        "run": lambda: solution(["WordDictionary","addWord","search"], [[],["ab"],["..."]]),
        "expected": [None, None, False],
    },
    {
        "description": "Exact match",
        "run": lambda: solution(["WordDictionary","addWord","search"], [[],["test"],["test"]]),
        "expected": [None, None, True],
    },
    {
        "description": "All dots match",
        "run": lambda: solution(["WordDictionary","addWord","search"], [[],["abc"],["..."]]),
        "expected": [None, None, True],
    },
]
