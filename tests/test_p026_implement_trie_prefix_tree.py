from problems.p026_implement_trie_prefix_tree import solution


def _run_trie_test():
    trie = solution()
    trie.insert("apple")
    results = []
    results.append(trie.search("apple"))      # True
    results.append(trie.search("app"))         # False
    results.append(trie.startsWith("app"))     # True
    trie.insert("app")
    results.append(trie.search("app"))         # True
    return results


TEST_CASES = [
    {
        "description": "Insert 'apple', search/startsWith, then insert 'app'",
        "run": _run_trie_test,
        "expected": [True, False, True, True],
    },
]
