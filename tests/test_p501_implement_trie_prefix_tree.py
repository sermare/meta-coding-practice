from problems.p501_implement_trie_prefix_tree import solution

TEST_CASES = [
    {
        "description": "Basic insert and search",
        "run": lambda: solution(["Trie","insert","search","search","startsWith","insert","search"], [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]),
        "expected": [None, None, True, False, True, None, True],
    },
    {
        "description": "Search empty trie",
        "run": lambda: solution(["Trie","search"], [[],["a"]]),
        "expected": [None, False],
    },
    {
        "description": "Prefix check",
        "run": lambda: solution(["Trie","insert","startsWith","startsWith"], [[],["hello"],["hel"],["world"]]),
        "expected": [None, None, True, False],
    },
    {
        "description": "Multiple inserts",
        "run": lambda: solution(["Trie","insert","insert","search","search"], [[],["cat"],["car"],["cat"],["car"]]),
        "expected": [None, None, None, True, True],
    },
    {
        "description": "Empty string prefix",
        "run": lambda: solution(["Trie","insert","startsWith"], [[],["abc"],[""]]),
        "expected": [None, None, True],
    },
]
