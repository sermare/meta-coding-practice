from problems.p439_palindrome_partitioning import solution

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
        "description": "No palindrome partitions beyond singles: abc",
        "run": lambda: solution("abc"),
        "expected": [["a", "b", "c"]],
    },
    {
        "description": "Palindrome string: aba",
        "run": lambda: sorted(solution("aba")),
        "expected": sorted([["a", "b", "a"], ["aba"]]),
    },
]
