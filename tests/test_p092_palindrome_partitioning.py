from problems.p092_palindrome_partitioning import solution

TEST_CASES = [
    {
        "description": "Basic: aab",
        "run": lambda: sorted(solution("aab")),
        "expected": sorted([["a", "a", "b"], ["aa", "b"]]),
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": [["a"]],
    },
    {
        "description": "All same: aaa",
        "run": lambda: sorted(solution("aaa")),
        "expected": sorted([["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    },
    {
        "description": "No multi-char palindromes: abc",
        "run": lambda: solution("abc"),
        "expected": [["a", "b", "c"]],
    },
]
